# `_SBDisplayPredicate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDisplayModePredicate`
- 2 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSString" _displayHardwareIdentifier;
@"NSString" _displayProductName;
```

## Class methods

```
+[_SBDisplayPredicate fromDefaultsKey:];
```

## Instance methods

```
-[_SBDisplayPredicate initWithDisplay:];
-[_SBDisplayPredicate hash];
-[_SBDisplayPredicate description];
-[_SBDisplayPredicate isEqual:];
-[_SBDisplayPredicate matchesDisplay:];
-[_SBDisplayPredicate defaultsKeyRepresentation];
-[_SBDisplayPredicate initWithDisplayHardwareIdentifier:productName:];
```
