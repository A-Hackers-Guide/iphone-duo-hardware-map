# `AVContentKeySpecifier`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSString" _keySystem;
@ _identifier;
@"NSDictionary" _options;
@"NSData" _initializationData;
```

## Properties

```
@property (T@"NSData",R) initializationData;
@property (T@"NSString",R,V_keySystem) keySystem;
@property (T@,R,V_identifier) identifier;
@property (T@"NSDictionary",R,V_options) options;
```

## Class methods

```
+[AVContentKeySpecifier contentKeySpecifierForKeySystem:identifier:options:];
```

## Instance methods

```
-[AVContentKeySpecifier identifier];
-[AVContentKeySpecifier dealloc];
-[AVContentKeySpecifier keySystem];
-[AVContentKeySpecifier options];
-[AVContentKeySpecifier copyWithZone:];
-[AVContentKeySpecifier initForKeySystem:identifier:initializationData:options:];
-[AVContentKeySpecifier initForKeySystem:identifier:options:];
-[AVContentKeySpecifier initForKeySystem:initializationData:];
-[AVContentKeySpecifier initializationData];
```
