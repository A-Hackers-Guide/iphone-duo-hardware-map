# `LAPSErrorBuilder`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 22 class methods

## Class methods

```
+[LAPSErrorBuilder errorWithCode:userInfo:];
+[LAPSErrorBuilder userCanceledError];
+[LAPSErrorBuilder genericError];
+[LAPSErrorBuilder _errorWithCode:debugDescription:];
+[LAPSErrorBuilder genericErrorWithDebugDescription:];
+[LAPSErrorBuilder genericErrorWithUnderlyingError:];
+[LAPSErrorBuilder deniedByLAError];
+[LAPSErrorBuilder errorWithError:];
+[LAPSErrorBuilder _genericErrorWithDebugDescription:];
+[LAPSErrorBuilder _genericErrorWithUserInfo:];
+[LAPSErrorBuilder checkError:hasCode:];
+[LAPSErrorBuilder checkErrorIsInteractive:];
+[LAPSErrorBuilder clientCanceledError];
+[LAPSErrorBuilder deniedByMDMError];
+[LAPSErrorBuilder genericErrorWithUnderlyingError:debugDescription:];
+[LAPSErrorBuilder invalidPasscodeError];
+[LAPSErrorBuilder invalidPasscodeErrorWithFailedAttemptsCount:];
+[LAPSErrorBuilder invalidPasscodeErrorWithFailedAttemptsCount:backoffTimeout:];
+[LAPSErrorBuilder newPasscodeDoesNotMeetRequirementsErrorWithLocalizedDescription:];
+[LAPSErrorBuilder newPasscodeIsTooEasyError];
+[LAPSErrorBuilder systemCanceledErrorWithDebugDescription:];
+[LAPSErrorBuilder tooManyAttemptsError];
```
