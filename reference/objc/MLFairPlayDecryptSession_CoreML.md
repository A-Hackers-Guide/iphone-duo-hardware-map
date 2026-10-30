# `MLFairPlayDecryptSession`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSString" _modelPath;
@"NSXPCConnection" _xpcConnection;
@"NSObject<CoreMLModelSecurityProtocol>" _xpcProxy;
```

## Properties

```
@property (T@"NSString",C,N,V_modelPath) modelPath;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (T@"NSObject<CoreMLModelSecurityProtocol>",&,N,V_xpcProxy) xpcProxy;
```

## Class methods

```
+[MLFairPlayDecryptSession decryptSessionForModelAtPath:usesCodeSigningIdentityForEncryption:keyBlob:error:];
```

## Instance methods

```
-[MLFairPlayDecryptSession setXpcConnection:];
-[MLFairPlayDecryptSession dealloc];
-[MLFairPlayDecryptSession modelPath];
-[MLFairPlayDecryptSession xpcConnection];
-[MLFairPlayDecryptSession setModelPath:];
-[MLFairPlayDecryptSession setXpcProxy:];
-[MLFairPlayDecryptSession xpcProxy];
```
