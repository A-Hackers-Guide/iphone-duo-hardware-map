# `CTLazuliMessageGroupFileTransferPush`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"CTLazuliGroupChatInformation" _chatInformation;
@"CTLazuliFileTransferDescriptor" _descriptor;
@"CTLazuliCustomMetaData" _metaData;
```

## Properties

```
@property (T@"CTLazuliGroupChatInformation",&,N,V_chatInformation) chatInformation;
@property (T@"CTLazuliFileTransferDescriptor",&,N,V_descriptor) descriptor;
@property (T@"CTLazuliCustomMetaData",&,N,V_metaData) metaData;
```

## Class methods

```
+[CTLazuliMessageGroupFileTransferPush supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliMessageGroupFileTransferPush setDescriptor:];
-[CTLazuliMessageGroupFileTransferPush setMetaData:];
-[CTLazuliMessageGroupFileTransferPush descriptor];
-[CTLazuliMessageGroupFileTransferPush metaData];
-[CTLazuliMessageGroupFileTransferPush encodeWithCoder:];
-[CTLazuliMessageGroupFileTransferPush description];
-[CTLazuliMessageGroupFileTransferPush initWithCoder:];
-[CTLazuliMessageGroupFileTransferPush copyWithZone:];
-[CTLazuliMessageGroupFileTransferPush isEqual:];
-[CTLazuliMessageGroupFileTransferPush chatInformation];
-[CTLazuliMessageGroupFileTransferPush initWithReflection:];
-[CTLazuliMessageGroupFileTransferPush isEqualToCTLazuliMessageGroupFileTransferPush:];
-[CTLazuliMessageGroupFileTransferPush setChatInformation:];
```
