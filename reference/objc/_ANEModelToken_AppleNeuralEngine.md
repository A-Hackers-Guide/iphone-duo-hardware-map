# `_ANEModelToken`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 7 class methods

## Instance variables

```
i _processIdentifier;
@"NSString" _modelIdentifier;
@"NSString" _csIdentity;
@"NSString" _teamIdentity;
```

## Properties

```
@property (T@"NSString",R,N,V_modelIdentifier) modelIdentifier;
@property (T@"NSString",R,N,V_csIdentity) csIdentity;
@property (T@"NSString",R,N,V_teamIdentity) teamIdentity;
@property (Ti,R,N,V_processIdentifier) processIdentifier;
```

## Class methods

```
+[_ANEModelToken appGroupIdentifiersFor:processIdentifier:];
+[_ANEModelToken codeSigningIDFor:processIdentifier:];
+[_ANEModelToken processNameFor:identifier:];
+[_ANEModelToken teamIDFor:processIdentifier:];
+[_ANEModelToken teamScopedCodeSigningIDFor:processIdentifier:];
+[_ANEModelToken tokenWithAuditToken:modelIdentifier:processIdentifier:];
+[_ANEModelToken tokenWithCsIdentity:teamIdentity:modelIdentifier:processIdentifier:];
```

## Instance methods

```
-[_ANEModelToken modelIdentifier];
-[_ANEModelToken description];
-[_ANEModelToken processIdentifier];
-[_ANEModelToken csIdentity];
-[_ANEModelToken initWithAuditToken:modelIdentifier:processIdentifier:];
-[_ANEModelToken initWithCsIdentity:teamIdentity:modelIdentifier:processIdentifier:];
-[_ANEModelToken teamIdentity];
```
