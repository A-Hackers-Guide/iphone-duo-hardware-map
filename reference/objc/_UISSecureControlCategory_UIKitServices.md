# `_UISSecureControlCategory`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 1 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
(?="all"S""{?="type"b6"iconIndex"b5"labelIndex"b5}) _fields;
```

## Properties

```
@property (TQ,R,N) type;
@property (TI,R,N) secureName;
@property (TI,R,N) secureNameForDrawing;
@property (T@"NSString",R,N) iconGlyph;
@property (TB,R,N,GisValid) valid;
```

## Class methods

```
+[_UISSecureControlCategory supportsSecureCoding];
```

## Instance methods

```
-[_UISSecureControlCategory authenticationMessageContextForStyle:];
-[_UISSecureControlCategory type];
-[_UISSecureControlCategory secureName];
-[_UISSecureControlCategory encodeWithCoder:];
-[_UISSecureControlCategory isValid];
-[_UISSecureControlCategory hash];
-[_UISSecureControlCategory initWithCoder:];
-[_UISSecureControlCategory copyWithZone:];
-[_UISSecureControlCategory isEqual:];
-[_UISSecureControlCategory initWithType:iconIndex:labelIndex:];
-[_UISSecureControlCategory iconGlyph];
-[_UISSecureControlCategory secureNameForDrawing];
```
