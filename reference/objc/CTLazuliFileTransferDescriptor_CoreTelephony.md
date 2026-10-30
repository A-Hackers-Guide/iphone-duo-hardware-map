# `CTLazuliFileTransferDescriptor`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"CTLazuliFileThumbnailInformation" _thumbnail;
@"CTLazuliFileDispositionInformation" _file;
@"CTLazuliCustomMetaData" _metaData;
```

## Properties

```
@property (T@"CTLazuliFileThumbnailInformation",&,N,V_thumbnail) thumbnail;
@property (T@"CTLazuliFileDispositionInformation",&,N,V_file) file;
@property (T@"CTLazuliCustomMetaData",&,N,V_metaData) metaData;
```

## Class methods

```
+[CTLazuliFileTransferDescriptor supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliFileTransferDescriptor file];
-[CTLazuliFileTransferDescriptor setMetaData:];
-[CTLazuliFileTransferDescriptor metaData];
-[CTLazuliFileTransferDescriptor setThumbnail:];
-[CTLazuliFileTransferDescriptor encodeWithCoder:];
-[CTLazuliFileTransferDescriptor description];
-[CTLazuliFileTransferDescriptor thumbnail];
-[CTLazuliFileTransferDescriptor initWithCoder:];
-[CTLazuliFileTransferDescriptor copyWithZone:];
-[CTLazuliFileTransferDescriptor isEqual:];
-[CTLazuliFileTransferDescriptor setFile:];
-[CTLazuliFileTransferDescriptor initWithReflection:];
-[CTLazuliFileTransferDescriptor isEqualToCTLazuliFileTransferDescriptor:];
```
