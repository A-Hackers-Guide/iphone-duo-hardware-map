# `AVCommonLoggingIdentifier`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVLoggingIdentifier`
- 2 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifierName;
I _derivedIdentifierCounter;
```

## Properties

```
@property (T@"NSString",R) name;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVCommonLoggingIdentifier dealloc];
-[AVCommonLoggingIdentifier initWithIdentifierSuffix:prefixlength:];
-[AVCommonLoggingIdentifier description];
-[AVCommonLoggingIdentifier makeDerivedIdentifier];
-[AVCommonLoggingIdentifier name];
```
