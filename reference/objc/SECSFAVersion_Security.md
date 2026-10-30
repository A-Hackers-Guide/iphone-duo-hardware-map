# `SECSFAVersion`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 8 properties, 27 instance methods, 0 class methods

## Instance variables

```
q _build;
q _major;
q _minor;
i _productName;
{?="build"b1"major"b1"minor"b1"productName"b1} _has;
```

## Properties

```
@property (TB,N) hasProductName;
@property (Ti,N,V_productName) productName;
@property (TB,N) hasMajor;
@property (Tq,N,V_major) major;
@property (TB,N) hasMinor;
@property (Tq,N,V_minor) minor;
@property (TB,N) hasBuild;
@property (Tq,N,V_build) build;
```

## Instance methods

```
-[SECSFAVersion major];
-[SECSFAVersion build];
-[SECSFAVersion writeTo:];
-[SECSFAVersion setProductName:];
-[SECSFAVersion productName];
-[SECSFAVersion hasProductName];
-[SECSFAVersion mergeFrom:];
-[SECSFAVersion setBuild:];
-[SECSFAVersion hasBuild];
-[SECSFAVersion minor];
-[SECSFAVersion hash];
-[SECSFAVersion copyTo:];
-[SECSFAVersion description];
-[SECSFAVersion readFrom:];
-[SECSFAVersion copyWithZone:];
-[SECSFAVersion isEqual:];
-[SECSFAVersion dictionaryRepresentation];
-[SECSFAVersion StringAsProductName:];
-[SECSFAVersion hasMajor];
-[SECSFAVersion hasMinor];
-[SECSFAVersion productNameAsString:];
-[SECSFAVersion setHasBuild:];
-[SECSFAVersion setHasMajor:];
-[SECSFAVersion setHasMinor:];
-[SECSFAVersion setHasProductName:];
-[SECSFAVersion setMajor:];
-[SECSFAVersion setMinor:];
```
