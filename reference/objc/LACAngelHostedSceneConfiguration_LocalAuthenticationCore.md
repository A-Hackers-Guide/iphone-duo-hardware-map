# `LACAngelHostedSceneConfiguration`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSString" _angelIdentifier;
@"NSXPCListenerEndpoint" _connectionEndpoint;
@"NSNumber" _evaluationRequestIdentifier;
@"NSString" _sceneIdentifier;
```

## Properties

```
@property (T@"NSString",R,N,V_angelIdentifier) angelIdentifier;
@property (T@"NSXPCListenerEndpoint",R,N,V_connectionEndpoint) connectionEndpoint;
@property (T@"NSNumber",R,N,V_evaluationRequestIdentifier) evaluationRequestIdentifier;
@property (T@"NSString",R,N,V_sceneIdentifier) sceneIdentifier;
```

## Class methods

```
+[LACAngelHostedSceneConfiguration supportsSecureCoding];
```

## Instance methods

```
-[LACAngelHostedSceneConfiguration sceneIdentifier];
-[LACAngelHostedSceneConfiguration encodeWithCoder:];
-[LACAngelHostedSceneConfiguration description];
-[LACAngelHostedSceneConfiguration initWithCoder:];
-[LACAngelHostedSceneConfiguration connectionEndpoint];
-[LACAngelHostedSceneConfiguration angelIdentifier];
-[LACAngelHostedSceneConfiguration evaluationRequestIdentifier];
-[LACAngelHostedSceneConfiguration initWithAngelIdentifier:sceneIdentifier:];
-[LACAngelHostedSceneConfiguration initWithAngelIdentifier:sceneIdentifier:endpoint:requestId:];
```
