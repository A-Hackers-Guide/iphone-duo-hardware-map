# `CKKSExternalTLKShare`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 12 instance methods, 3 class methods

## Instance variables

```
@"NSString" _view;
@"NSString" _tlkUUID;
@"NSData" _receiverPeerID;
@"NSData" _senderPeerID;
@"NSData" _wrappedTLK;
@"NSData" _signature;
```

## Properties

```
@property (T@"NSString",R,V_view) view;
@property (T@"NSString",R,V_tlkUUID) tlkUUID;
@property (T@"NSData",R,V_receiverPeerID) receiverPeerID;
@property (T@"NSData",R,V_senderPeerID) senderPeerID;
@property (T@"NSData",R,V_wrappedTLK) wrappedTLK;
@property (T@"NSData",R,V_signature) signature;
```

## Class methods

```
+[CKKSExternalTLKShare supportsSecureCoding];
+[CKKSExternalTLKShare parseFromJSONDict:error:];
+[CKKSExternalTLKShare unstringifyPeerID:];
```

## Instance methods

```
-[CKKSExternalTLKShare signature];
-[CKKSExternalTLKShare jsonDictionary];
-[CKKSExternalTLKShare view];
-[CKKSExternalTLKShare encodeWithCoder:];
-[CKKSExternalTLKShare description];
-[CKKSExternalTLKShare initWithCoder:];
-[CKKSExternalTLKShare tlkUUID];
-[CKKSExternalTLKShare initWithView:tlkUUID:receiverPeerID:senderPeerID:wrappedTLK:signature:];
-[CKKSExternalTLKShare receiverPeerID];
-[CKKSExternalTLKShare senderPeerID];
-[CKKSExternalTLKShare stringifyPeerID:];
-[CKKSExternalTLKShare wrappedTLK];
```
