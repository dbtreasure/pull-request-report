# Engineering Standards

## Code Organization Principles

### Feature-Based Organization
- **Mandatory**: All new code must follow feature-based organization
- **Structure**: `/feature/[components|services|models|tests]`
- **Rationale**: Improves maintainability and team collaboration

### Service Layer Patterns  
- **Service Classes**: Use static methods wrapped in classes
- **Separation of Concerns**: Business logic in services, HTTP concerns in routers
- **Example**:
  ```python
  class UserService:
      @staticmethod
      def create_user(data: UserCreateSchema) -> User:
          # Business logic here
          pass
  ```

## Repository Standards

### CRITICAL: Repository Layer Purity
- **ZERO business logic** allowed in repository/DAO layers
- **Pure database transactions** only
- **Type conversion** must happen in service layer, NOT repository layer
- **Violation**: Any business logic in DAO is a critical standards violation

### Database Object Usage
- **Prefer existing schemas** over creating new intermediate objects
- **Direct usage**: Use `UserRead` directly instead of creating `UserInfo` wrappers
- **Efficiency principle**: Minimize unnecessary data transformation layers

## API Design Standards

### Router Configuration
- **Mandatory fields**: `responses` and `redirect_slashes` must be explicitly declared
- **Consistency**: Follow established patterns across all routers
- **Example**:
  ```python
  router = APIRouter(
      prefix="/users",
      responses={404: {"description": "Not found"}},
      redirect_slashes=False
  )
  ```

### Error Handling
- **Consistent patterns**: Use established error handling utilities
- **Null safety**: Comprehensive null checks in all API endpoints
- **Defensive programming**: Especially for third-party integrations

## Code Quality Requirements

### DRY Principle (Don't Repeat Yourself)
- **Extract common logic** to utility modules
- **Avoid duplication** across similar implementations
- **Shared constants** for repeated strings and messages

### Modern Python Patterns
- **Prefer pathlib** over os.path
- **Type annotations** without unnecessary quotes
- **Static methods** when instance state isn't needed

### Testing Strategy
- **Smoke testing**: Reviewers must conduct thorough validation
- **Edge cases**: Consider all user states and transitions
- **Resource cleanup**: Use context managers for external resources

## Team Culture Standards

### Code Review Process
- **Constructive feedback**: Focus on improvement opportunities
- **Standards reference**: Explicitly mention documented standards during reviews
- **Collaborative approach**: Quick implementation of suggested improvements

### Performance Consciousness
- **Async optimization**: Leverage established async patterns like `gather_with_concurrency`
- **External API efficiency**: Minimize and optimize third-party API calls
- **Resource management**: Proper handling of database connections and external services