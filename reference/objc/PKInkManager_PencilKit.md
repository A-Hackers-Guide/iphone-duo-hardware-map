# `PKInkManager`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" _inks;
@"NSMutableDictionary" _supportedInkIdentifiers;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_inks) inks;
@property (T@"NSMutableDictionary",R,N,V_supportedInkIdentifiers) supportedInkIdentifiers;
```

## Class methods

```
+[PKInkManager clearCachedManager];
+[PKInkManager defaultInkManager];
```

## Instance methods

```
-[PKInkManager init];
-[PKInkManager addInkBehavior:forIdentifier:];
-[PKInkManager inkBehaviorForIdentifier:variant:];
-[PKInkManager inkBehaviorForIdentifier:version:variant:];
-[PKInkManager inks];
-[PKInkManager supportedInkIdentifierFromIdentifier:];
-[PKInkManager supportedInkIdentifiers];
```
