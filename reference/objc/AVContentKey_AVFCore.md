# `AVContentKey`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigContentKeyBoss=} _keyBoss;
^{OpaqueFigContentKeySpecifier=} _contentKeySpecifier;
^{OpaqueFigCPECryptor=} _cryptor;
@"AVContentKeySpecifier" contentKeySpecifier;
```

## Properties

```
@property (T@"AVContentKeySpecifier",R,VcontentKeySpecifier) contentKeySpecifier;
@property (Tq,R) externalContentProtectionStatus;
```

## Class methods

```
+[AVContentKey contentKeyWithSpecifier:cryptor:contentKeyBoss:contentKeySpecifier:];
```

## Instance methods

```
-[AVContentKey dealloc];
-[AVContentKey cryptor];
-[AVContentKey externalContentProtectionStatus];
-[AVContentKey _cryptorForFormatDescription:error:];
-[AVContentKey _internalContentKeySpecifier];
-[AVContentKey contentKeySpecifier];
-[AVContentKey cryptorForFormatDescription:error:];
-[AVContentKey initWithSpecifier:cryptor:contentKeyBoss:contentKeySpecifier:];
-[AVContentKey revoke];
```
