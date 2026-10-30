# `SBKeyboardFocusResolutionContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `BSDescriptionStreamable`
- 2 instance variables, 6 properties, 9 instance methods, 2 class methods

## Instance variables

```
B _screenDim;
@"SBFZStackResolver" _zStackResolver;
```

## Properties

```
@property (TB,R,N,GisScreenDim) screenDim;
@property (T@"SBFZStackResolver",R,N) zStackResolver;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBKeyboardFocusResolutionContext build:];
+[SBKeyboardFocusResolutionContext new];
```

## Instance methods

```
-[SBKeyboardFocusResolutionContext mutableCopyWithZone:];
-[SBKeyboardFocusResolutionContext init];
-[SBKeyboardFocusResolutionContext appendDescriptionToFormatter:];
-[SBKeyboardFocusResolutionContext hash];
-[SBKeyboardFocusResolutionContext description];
-[SBKeyboardFocusResolutionContext copyWithZone:];
-[SBKeyboardFocusResolutionContext isEqual:];
-[SBKeyboardFocusResolutionContext zStackResolver];
-[SBKeyboardFocusResolutionContext isScreenDim];
```
