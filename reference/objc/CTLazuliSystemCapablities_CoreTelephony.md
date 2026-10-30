# `CTLazuliSystemCapablities`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 23 instance methods, 1 class methods

## Instance variables

```
B _autoAcceptChat;
B _autoAcceptGroupChat;
B _fileTransferAutoAccept;
@"NSURL" _exploderUri;
@"NSNumber" _maxGroupSize;
@"NSURL" _fileTransferUrl;
@"NSNumber" _fileTransferMaxRecipients;
@"NSNumber" _maxFileTransferSize;
```

## Properties

```
@property (T@"NSURL",&,N,V_exploderUri) exploderUri;
@property (TB,N,V_autoAcceptChat) autoAcceptChat;
@property (TB,N,V_autoAcceptGroupChat) autoAcceptGroupChat;
@property (T@"NSNumber",&,N,V_maxGroupSize) maxGroupSize;
@property (T@"NSURL",&,N,V_fileTransferUrl) fileTransferUrl;
@property (T@"NSNumber",&,N,V_fileTransferMaxRecipients) fileTransferMaxRecipients;
@property (T@"NSNumber",&,N,V_maxFileTransferSize) maxFileTransferSize;
@property (TB,N,V_fileTransferAutoAccept) fileTransferAutoAccept;
```

## Class methods

```
+[CTLazuliSystemCapablities supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliSystemCapablities encodeWithCoder:];
-[CTLazuliSystemCapablities description];
-[CTLazuliSystemCapablities initWithCoder:];
-[CTLazuliSystemCapablities copyWithZone:];
-[CTLazuliSystemCapablities isEqual:];
-[CTLazuliSystemCapablities fileTransferUrl];
-[CTLazuliSystemCapablities setExploderUri:];
-[CTLazuliSystemCapablities autoAcceptChat];
-[CTLazuliSystemCapablities autoAcceptGroupChat];
-[CTLazuliSystemCapablities exploderUri];
-[CTLazuliSystemCapablities fileTransferAutoAccept];
-[CTLazuliSystemCapablities fileTransferMaxRecipients];
-[CTLazuliSystemCapablities initWithReflection:];
-[CTLazuliSystemCapablities isEqualToCTLazuliSystemCapablities:];
-[CTLazuliSystemCapablities maxFileTransferSize];
-[CTLazuliSystemCapablities maxGroupSize];
-[CTLazuliSystemCapablities setAutoAcceptChat:];
-[CTLazuliSystemCapablities setAutoAcceptGroupChat:];
-[CTLazuliSystemCapablities setFileTransferAutoAccept:];
-[CTLazuliSystemCapablities setFileTransferMaxRecipients:];
-[CTLazuliSystemCapablities setFileTransferUrl:];
-[CTLazuliSystemCapablities setMaxFileTransferSize:];
-[CTLazuliSystemCapablities setMaxGroupSize:];
```
