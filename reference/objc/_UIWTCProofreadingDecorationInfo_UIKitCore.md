# `_UIWTCProofreadingDecorationInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSUUID" _identifier;
@"NSArray" _ranges;
@"NSDictionary" _paths;
@"NSMapTable" _containers;
q _type;
```

## Properties

```
@property (T@"NSUUID",R,N,V_identifier) identifier;
@property (T@"NSArray",R,N,V_ranges) ranges;
@property (T@"NSDictionary",R,N,V_paths) paths;
@property (T@"NSMapTable",R,N,V_containers) containers;
@property (Tq,R,N,V_type) type;
```

## Class methods

```
+[_UIWTCProofreadingDecorationInfo highlightInfoWithIdentifier:ranges:decorationPaths:containers:];
+[_UIWTCProofreadingDecorationInfo underlineInfoWithIdentifier:ranges:decorationPaths:containers:];
```

## Instance methods

```
-[_UIWTCProofreadingDecorationInfo ranges];
-[_UIWTCProofreadingDecorationInfo identifier];
-[_UIWTCProofreadingDecorationInfo type];
-[_UIWTCProofreadingDecorationInfo description];
-[_UIWTCProofreadingDecorationInfo paths];
-[_UIWTCProofreadingDecorationInfo containers];
-[_UIWTCProofreadingDecorationInfo addPaths:withContainer:forRange:];
-[_UIWTCProofreadingDecorationInfo initWithType:identifier:ranges:decorationPaths:containers:];
```
