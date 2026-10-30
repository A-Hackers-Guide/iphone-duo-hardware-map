# `_UISSecureControlSizeSpec`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSString" _localization;
(?="all"S""{?="arrangeVertically"b1"accessibilityContrast"b1"displayScale"b3"layoutDirection"b1"legibilityWeight"b1"preferredContentSizeCategory"b4"userInterfaceIdiom"b3}) _fields;
@"_UISSecureControlCategory" _category;
```

## Properties

```
@property (T@"_UISSecureControlCategory",R,N,V_category) category;
@property (T@"UISSlotStyle",R,N) style;
@property (TB,R,N) arrangeVertically;
```

## Class methods

```
+[_UISSecureControlSizeSpec supportsSecureCoding];
+[_UISSecureControlSizeSpec specWithStyle:tag:];
```

## Instance methods

```
-[_UISSecureControlSizeSpec category];
-[_UISSecureControlSizeSpec style];
-[_UISSecureControlSizeSpec encodeWithCoder:];
-[_UISSecureControlSizeSpec hash];
-[_UISSecureControlSizeSpec initWithCoder:];
-[_UISSecureControlSizeSpec copyWithZone:];
-[_UISSecureControlSizeSpec isEqual:];
-[_UISSecureControlSizeSpec isEquivalentToStyle:tag:];
-[_UISSecureControlSizeSpec arrangeVertically];
-[_UISSecureControlSizeSpec initWithCategory:arrangeVertically:accessibilityContrast:displayScale:layoutDirection:legibilityWeight:localization:preferredContentSizeCategory:userInterfaceIdiom:];
```
