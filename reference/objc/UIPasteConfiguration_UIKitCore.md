# `UIPasteConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 1 instance variables, 2 properties, 14 instance methods, 4 class methods

## Instance variables

```
@"NSMutableOrderedSet" _acceptableTypes;
```

## Properties

```
@property (T@"NSArray",C,D,N) acceptableTypes;
@property (T@"NSArray",C,D,N) acceptableTypeIdentifiers;
```

## Class methods

```
+[UIPasteConfiguration supportsSecureCoding];
+[UIPasteConfiguration _pasteConfigurationForAcceptingClasses:];
+[UIPasteConfiguration pasteConfigurationForAcceptingClasses:];
+[UIPasteConfiguration pasteConfigurationWithAcceptableTypes:];
```

## Instance methods

```
-[UIPasteConfiguration setAcceptableTypes:];
-[UIPasteConfiguration init];
-[UIPasteConfiguration addTypeIdentifiersForAcceptingClass:];
-[UIPasteConfiguration initWithAcceptableTypeIdentifiers:];
-[UIPasteConfiguration acceptableTypes];
-[UIPasteConfiguration addAcceptableTypeIdentifiers:];
-[UIPasteConfiguration initWithAcceptableTypes:];
-[UIPasteConfiguration encodeWithCoder:];
-[UIPasteConfiguration setAcceptableTypeIdentifiers:];
-[UIPasteConfiguration initWithTypeIdentifiersForAcceptingClass:];
-[UIPasteConfiguration initWithCoder:];
-[UIPasteConfiguration copyWithZone:];
-[UIPasteConfiguration isEqual:];
-[UIPasteConfiguration acceptableTypeIdentifiers];
```
