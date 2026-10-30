# `CTStewieCompressionResult`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _isPreferredCodec;
@"NSData" _compressedData;
q _codecId;
```

## Properties

```
@property (T@"NSData",&,N,V_compressedData) compressedData;
@property (Tq,N,V_codecId) codecId;
@property (TB,N,V_isPreferredCodec) isPreferredCodec;
```

## Class methods

```
+[CTStewieCompressionResult supportsSecureCoding];
```

## Instance methods

```
-[CTStewieCompressionResult encodeWithCoder:];
-[CTStewieCompressionResult description];
-[CTStewieCompressionResult initWithCoder:];
-[CTStewieCompressionResult copyWithZone:];
-[CTStewieCompressionResult isEqual:];
-[CTStewieCompressionResult compressedData];
-[CTStewieCompressionResult codecId];
-[CTStewieCompressionResult isPreferredCodec];
-[CTStewieCompressionResult setCodecId:];
-[CTStewieCompressionResult setCompressedData:];
-[CTStewieCompressionResult setIsPreferredCodec:];
```
