# `SBFDisplayToolSystemSpace`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 8 instance methods, 2 class methods

## Instance variables

```
q _kind;
q _overlay;
@"NSString" _bundleIdentifier;
```

## Properties

```
@property (Tq,R,N,V_kind) kind;
@property (Tq,R,N,V_overlay) overlay;
@property (T@"NSString",R,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",R,N) baseName;
@property (T@"NSString",R,N) name;
```

## Class methods

```
+[SBFDisplayToolSystemSpace systemSpaceFromDictionary:];
+[SBFDisplayToolSystemSpace systemSpaceFromString:error:];
```

## Instance methods

```
-[SBFDisplayToolSystemSpace bundleIdentifier];
-[SBFDisplayToolSystemSpace overlay];
-[SBFDisplayToolSystemSpace description];
-[SBFDisplayToolSystemSpace name];
-[SBFDisplayToolSystemSpace kind];
-[SBFDisplayToolSystemSpace dictionaryRepresentation];
-[SBFDisplayToolSystemSpace _initWithKind:overlay:bundleIdentifier:];
-[SBFDisplayToolSystemSpace baseName];
```
