# `UIDocumentErrorRecoveryAttempter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"UIDocument" _document;
@ _wrappedRecoveryAttempter;
@? _continuerOrNil;
q _silentRecoveryOptionIndex;
@? _appModalRecoveryAttempter;
@? _recoveryCancelerOrNil;
{?="attemptedRecovery"b1} _errorRecoveryAttempterFlags;
```

## Instance methods

```
-[UIDocumentErrorRecoveryAttempter dealloc];
-[UIDocumentErrorRecoveryAttempter attemptRecoveryFromError:optionIndex:];
-[UIDocumentErrorRecoveryAttempter attemptSilentRecoveryFromError:error:];
-[UIDocumentErrorRecoveryAttempter cancelRecovery];
-[UIDocumentErrorRecoveryAttempter initWithDocument:silentRecoveryOptionIndex:appModalRecoveryAttempter:recoveryCanceler:];
-[UIDocumentErrorRecoveryAttempter initWithDocument:wrappedRecoveryAttempter:];
```
