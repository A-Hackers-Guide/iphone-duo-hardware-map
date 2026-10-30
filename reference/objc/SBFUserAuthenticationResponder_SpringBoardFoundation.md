# `SBFUserAuthenticationResponder`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFAuthenticationResponder`
- 3 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
@? _successHandler;
@? _failureHandler;
@? _invalidHandler;
```

## Properties

```
@property (T@?,C,N,V_successHandler) successHandler;
@property (T@?,C,N,V_failureHandler) failureHandler;
@property (T@?,C,N,V_invalidHandler) invalidHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFUserAuthenticationResponder responderWithSuccessHandler:failureHandler:invalidHandler:];
```

## Instance methods

```
-[SBFUserAuthenticationResponder failureHandler];
-[SBFUserAuthenticationResponder handleFailedAuthenticationRequest:error:];
-[SBFUserAuthenticationResponder handleInvalidAuthenticationRequest:];
-[SBFUserAuthenticationResponder handleSuccessfulAuthenticationRequest:];
-[SBFUserAuthenticationResponder initWithSuccessHandler:failureHandler:invalidHandler:];
-[SBFUserAuthenticationResponder invalidHandler];
-[SBFUserAuthenticationResponder setFailureHandler:];
-[SBFUserAuthenticationResponder setInvalidHandler:];
-[SBFUserAuthenticationResponder setSuccessHandler:];
-[SBFUserAuthenticationResponder successHandler];
```
