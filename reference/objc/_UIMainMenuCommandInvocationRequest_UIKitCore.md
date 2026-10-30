# `_UIMainMenuCommandInvocationRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 7 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"_UIMainMenuCommand" _providedCommand;
@"_UIMainMenuSession" _providedSession;
@"_UIMainMenuCommandIdentifier" _commandIdentifier;
@"_UIMainMenuSessionIdentifier" _sessionIdentifier;
@"_UISystemAuthenticationServiceMessage" _systemAuthenticationServiceMessage;
@"_UIMainMenuSessionRequest" _sessionRequest;
```

## Properties

```
@property (T@"_UIMainMenuCommandIdentifier",R,N,V_commandIdentifier) _commandIdentifier;
@property (T@"_UIMainMenuSessionIdentifier",R,N,V_sessionIdentifier) _sessionIdentifier;
@property (T@"_UIMainMenuCommand",R,N) command;
@property (T@"_UIMainMenuSession",R,N) session;
@property (T@"_UISystemAuthenticationServiceMessage",&,N,V_systemAuthenticationServiceMessage) systemAuthenticationServiceMessage;
@property (T@"BKSHIDEventAuthenticationMessage",&,N) authenticationMessage;
@property (T@"_UIMainMenuSessionRequest",&,N,V_sessionRequest) sessionRequest;
```

## Class methods

```
+[_UIMainMenuCommandInvocationRequest supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuCommandInvocationRequest authenticationMessage];
-[_UIMainMenuCommandInvocationRequest command];
-[_UIMainMenuCommandInvocationRequest setAuthenticationMessage:];
-[_UIMainMenuCommandInvocationRequest encodeWithCoder:];
-[_UIMainMenuCommandInvocationRequest hash];
-[_UIMainMenuCommandInvocationRequest description];
-[_UIMainMenuCommandInvocationRequest initWithCoder:];
-[_UIMainMenuCommandInvocationRequest session];
-[_UIMainMenuCommandInvocationRequest isEqual:];
-[_UIMainMenuCommandInvocationRequest _sessionIdentifier];
-[_UIMainMenuCommandInvocationRequest _commandIdentifier];
-[_UIMainMenuCommandInvocationRequest initWithCommand:session:];
-[_UIMainMenuCommandInvocationRequest sessionRequest];
-[_UIMainMenuCommandInvocationRequest setSessionRequest:];
-[_UIMainMenuCommandInvocationRequest setSystemAuthenticationServiceMessage:];
-[_UIMainMenuCommandInvocationRequest systemAuthenticationServiceMessage];
```
