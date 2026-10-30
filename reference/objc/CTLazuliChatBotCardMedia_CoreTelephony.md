# `CTLazuliChatBotCardMedia`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSURL" _mediaUrl;
@"NSString" _mediaContentType;
@"NSNumber" _mediaFileSize;
@"NSURL" _thumbnailUrl;
@"NSString" _thumbnailContentType;
@"NSNumber" _thumbnailFileSize;
q _height;
@"NSString" _contentDescription;
```

## Properties

```
@property (T@"NSURL",&,N,V_mediaUrl) mediaUrl;
@property (T@"NSString",&,N,V_mediaContentType) mediaContentType;
@property (T@"NSNumber",&,N,V_mediaFileSize) mediaFileSize;
@property (T@"NSURL",&,N,V_thumbnailUrl) thumbnailUrl;
@property (T@"NSString",&,N,V_thumbnailContentType) thumbnailContentType;
@property (T@"NSNumber",&,N,V_thumbnailFileSize) thumbnailFileSize;
@property (Tq,N,V_height) height;
@property (T@"NSString",&,N,V_contentDescription) contentDescription;
```

## Class methods

```
+[CTLazuliChatBotCardMedia supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliChatBotCardMedia contentDescription];
-[CTLazuliChatBotCardMedia setContentDescription:];
-[CTLazuliChatBotCardMedia setHeight:];
-[CTLazuliChatBotCardMedia encodeWithCoder:];
-[CTLazuliChatBotCardMedia description];
-[CTLazuliChatBotCardMedia initWithCoder:];
-[CTLazuliChatBotCardMedia copyWithZone:];
-[CTLazuliChatBotCardMedia isEqual:];
-[CTLazuliChatBotCardMedia height];
-[CTLazuliChatBotCardMedia setThumbnailContentType:];
-[CTLazuliChatBotCardMedia thumbnailContentType];
-[CTLazuliChatBotCardMedia mediaContentType];
-[CTLazuliChatBotCardMedia mediaUrl];
-[CTLazuliChatBotCardMedia thumbnailUrl];
-[CTLazuliChatBotCardMedia initWithReflection:];
-[CTLazuliChatBotCardMedia isEqualToCTLazuliChatBotCardMedia:];
-[CTLazuliChatBotCardMedia mediaFileSize];
-[CTLazuliChatBotCardMedia setMediaContentType:];
-[CTLazuliChatBotCardMedia setMediaFileSize:];
-[CTLazuliChatBotCardMedia setMediaUrl:];
-[CTLazuliChatBotCardMedia setThumbnailFileSize:];
-[CTLazuliChatBotCardMedia setThumbnailUrl:];
-[CTLazuliChatBotCardMedia thumbnailFileSize];
```
