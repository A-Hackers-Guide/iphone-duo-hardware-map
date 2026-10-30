# `KCJoiningMessage`

- Image: [`/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`](../userland/System__Library__PrivateFrameworks__KeychainCircle.framework__KeychainCircle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 6 class methods

## Instance variables

```
i _type;
@"NSData" _firstData;
@"NSData" _secondData;
@"NSData" _der;
```

## Properties

```
@property (Ti,R,V_type) type;
@property (T@"NSData",R,V_firstData) firstData;
@property (T@"NSData",R,V_secondData) secondData;
@property (T@"NSData",R,V_der) der;
```

## Class methods

```
+[KCJoiningMessage encodeToDERType:data:payload:error:];
+[KCJoiningMessage encodedSizeType:data:payload:error:];
+[KCJoiningMessage messageWithDER:error:];
+[KCJoiningMessage messageWithType:data:error:];
+[KCJoiningMessage messageWithType:data:payload:error:];
+[KCJoiningMessage messageWithType:data:secondData:error:];
```

## Instance methods

```
-[KCJoiningMessage type];
-[KCJoiningMessage der];
-[KCJoiningMessage firstData];
-[KCJoiningMessage inflatePartsOfEncoding:];
-[KCJoiningMessage initWithDER:error:];
-[KCJoiningMessage initWithType:data:payload:error:];
-[KCJoiningMessage secondData];
```
