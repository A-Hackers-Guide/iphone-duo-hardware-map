# `_UISSecureControlTag`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UISSlotTag`
- Protocols: `NSSecureCoding`
- 7 instance variables, 7 properties, 20 instance methods, 2 class methods

## Instance variables

```
@"_UISSecureControlCategory" _category;
d _cornerRadius;
q _cornerStyle;
^{CGColor=} _baseForegroundColor;
^{CGColor=} _baseBackgroundColor;
Q _imagePlacement;
{CGSize="width"d"height"d} _size;
```

## Properties

```
@property (T@"_UISSecureControlCategory",R,N,V_category) category;
@property (Td,R,N,V_cornerRadius) cornerRadius;
@property (Tq,R,N,V_cornerStyle) cornerStyle;
@property (T^{CGColor=},R,N,V_baseForegroundColor) baseForegroundColor;
@property (T^{CGColor=},R,N,V_baseBackgroundColor) baseBackgroundColor;
@property (TQ,R,N,V_imagePlacement) imagePlacement;
@property (T{CGSize=dd},R,N,V_size) size;
```

## Class methods

```
+[_UISSecureControlTag supportsSecureCoding];
+[_UISSecureControlTag cacheLimit];
```

## Instance methods

```
-[_UISSecureControlTag cornerStyle];
-[_UISSecureControlTag resolvedStyleForStyle:];
-[_UISSecureControlTag category];
-[_UISSecureControlTag dealloc];
-[_UISSecureControlTag secureNameForStyle:];
-[_UISSecureControlTag size];
-[_UISSecureControlTag authenticationMessageContextForStyle:];
-[_UISSecureControlTag cornerRadius];
-[_UISSecureControlTag encodeWithCoder:];
-[_UISSecureControlTag isValid];
-[_UISSecureControlTag hash];
-[_UISSecureControlTag initWithCoder:];
-[_UISSecureControlTag copyWithZone:];
-[_UISSecureControlTag isEqual:];
-[_UISSecureControlTag baseBackgroundColor];
-[_UISSecureControlTag baseForegroundColor];
-[_UISSecureControlTag imagePlacement];
-[_UISSecureControlTag initWithCategory:cornerStyle:cornerRadius:baseForegroundColor:baseBackgroundColor:imagePlacement:size:];
-[_UISSecureControlTag hitTestInformationMaskForStyle:];
-[_UISSecureControlTag failGradeForStyle:];
```
