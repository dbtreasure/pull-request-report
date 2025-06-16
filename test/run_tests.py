#!/usr/bin/env python3
"""
Test runner for Pull Request Report tool
Runs all tests and provides comprehensive reporting
"""

import sys
import subprocess
import importlib.util
from pathlib import Path
import time


def run_python_file(file_path):
    """Run a Python test file and capture results"""
    print(f"🧪 Running {file_path.name}...")
    start_time = time.time()
    
    try:
        # Run the file as a subprocess for cleaner output
        result = subprocess.run([
            sys.executable, str(file_path)
        ], capture_output=True, text=True, cwd=file_path.parent)
        
        duration = time.time() - start_time
        
        if result.returncode == 0:
            print(f"   ✅ PASSED ({duration:.2f}s)")
            if result.stdout.strip():
                for line in result.stdout.strip().split('\n'):
                    if line.strip():
                        print(f"   📝 {line}")
            return True, None
        else:
            print(f"   ❌ FAILED ({duration:.2f}s)")
            error_msg = result.stderr or result.stdout
            return False, error_msg
            
    except Exception as e:
        duration = time.time() - start_time
        print(f"   💥 ERROR ({duration:.2f}s)")
        return False, str(e)


def main():
    """Run all tests"""
    print("🚀 Pull Request Report - Test Suite")
    print("=" * 50)
    
    test_root = Path(__file__).parent
    
    # Find all test files
    unit_tests = list((test_root / "unit").glob("test_*.py"))
    integration_tests = list((test_root / "integration").glob("test_*.py"))
    
    all_tests = []
    all_tests.extend(("Unit", test) for test in unit_tests)
    all_tests.extend(("Integration", test) for test in integration_tests)
    
    if not all_tests:
        print("❌ No test files found!")
        return 1
    
    print(f"📋 Found {len(all_tests)} test files")
    print()
    
    # Run tests
    passed = 0
    failed = 0
    errors = []
    
    for test_type, test_file in all_tests:
        print(f"[{test_type}] {test_file.stem}")
        success, error = run_python_file(test_file)
        
        if success:
            passed += 1
        else:
            failed += 1
            errors.append((test_file.name, error))
        
        print()
    
    # Summary
    print("=" * 50)
    print("📊 Test Results Summary")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"📈 Success Rate: {passed/(passed+failed)*100:.1f}%")
    
    if errors:
        print("\n💥 Failures:")
        for test_name, error in errors:
            print(f"\n{test_name}:")
            # Show first few lines of error
            error_lines = error.strip().split('\n')[:5]
            for line in error_lines:
                print(f"  {line}")
            if len(error.strip().split('\n')) > 5:
                print("  ...")
    
    print("\n" + "=" * 50)
    
    if failed == 0:
        print("🎉 All tests passed!")
        return 0
    else:
        print(f"💔 {failed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())