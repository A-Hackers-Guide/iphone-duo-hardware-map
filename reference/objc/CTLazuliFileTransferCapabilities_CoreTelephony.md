# `CTLazuliFileTransferCapabilities`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 10 instance variables, 10 properties, 27 instance methods, 1 class methods

## Instance variables

```
B _autoAccept;
B _httpFallback;
@"NSURL" _url;
@"NSURL" _contentServerUploadUrl;
@"NSURL" _contentServerDownloadUrl;
@"NSString" _userName;
@"NSString" _password;
@"NSNumber" _max1ToManyRecipients;
@"NSNumber" _maxTransferSize;
@"NSNumber" _warnSize;
```

## Properties

```
@property (T@"NSURL",&,N,V_url) url;
@property (T@"NSURL",&,N,V_contentServerUploadUrl) contentServerUploadUrl;
@property (T@"NSURL",&,N,V_contentServerDownloadUrl) contentServerDownloadUrl;
@property (T@"NSString",&,N,V_userName) userName;
@property (T@"NSString",&,N,V_password) password;
@property (T@"NSNumber",&,N,V_max1ToManyRecipients) max1ToManyRecipients;
@property (T@"NSNumber",&,N,V_maxTransferSize) maxTransferSize;
@property (TB,N,V_autoAccept) autoAccept;
@property (TB,N,V_httpFallback) httpFallback;
@property (T@"NSNumber",&,N,V_warnSize) warnSize;
```

## Class methods

```
+[CTLazuliFileTransferCapabilities supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliFileTransferCapabilities userName];
-[CTLazuliFileTransferCapabilities encodeWithCoder:];
-[CTLazuliFileTransferCapabilities description];
-[CTLazuliFileTransferCapabilities initWithCoder:];
-[CTLazuliFileTransferCapabilities setUrl:];
-[CTLazuliFileTransferCapabilities setPassword:];
-[CTLazuliFileTransferCapabilities copyWithZone:];
-[CTLazuliFileTransferCapabilities isEqual:];
-[CTLazuliFileTransferCapabilities password];
-[CTLazuliFileTransferCapabilities url];
-[CTLazuliFileTransferCapabilities setUserName:];
-[CTLazuliFileTransferCapabilities maxTransferSize];
-[CTLazuliFileTransferCapabilities autoAccept];
-[CTLazuliFileTransferCapabilities contentServerDownloadUrl];
-[CTLazuliFileTransferCapabilities contentServerUploadUrl];
-[CTLazuliFileTransferCapabilities httpFallback];
-[CTLazuliFileTransferCapabilities initWithReflection:];
-[CTLazuliFileTransferCapabilities isEqualToCTLazuliFileTransferCapabilities:];
-[CTLazuliFileTransferCapabilities max1ToManyRecipients];
-[CTLazuliFileTransferCapabilities setAutoAccept:];
-[CTLazuliFileTransferCapabilities setContentServerDownloadUrl:];
-[CTLazuliFileTransferCapabilities setContentServerUploadUrl:];
-[CTLazuliFileTransferCapabilities setHttpFallback:];
-[CTLazuliFileTransferCapabilities setMax1ToManyRecipients:];
-[CTLazuliFileTransferCapabilities setMaxTransferSize:];
-[CTLazuliFileTransferCapabilities setWarnSize:];
-[CTLazuliFileTransferCapabilities warnSize];
```
