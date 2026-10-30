# `CKKSExternalKey`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSString" _view;
@"NSString" _uuid;
@"NSString" _parentKeyUUID;
@"NSData" _keyData;
```

## Properties

```
@property (T@"NSString",R,V_view) view;
@property (T@"NSString",R,V_uuid) uuid;
@property (T@"NSString",R,V_parentKeyUUID) parentKeyUUID;
@property (T@"NSData",R,V_keyData) keyData;
```

## Class methods

```
+[CKKSExternalKey supportsSecureCoding];
+[CKKSExternalKey parseFromJSONDict:error:];
```

## Instance methods

```
-[CKKSExternalKey uuid];
-[CKKSExternalKey jsonDictionary];
-[CKKSExternalKey view];
-[CKKSExternalKey encodeWithCoder:];
-[CKKSExternalKey description];
-[CKKSExternalKey initWithCoder:];
-[CKKSExternalKey isEqual:];
-[CKKSExternalKey keyData];
-[CKKSExternalKey initWithView:uuid:parentTLKUUID:keyData:];
-[CKKSExternalKey parentKeyUUID];
```
