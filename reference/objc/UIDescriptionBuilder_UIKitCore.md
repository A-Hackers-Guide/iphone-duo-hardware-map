# `UIDescriptionBuilder`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 22 instance methods, 3 class methods

## Instance variables

```
@"NSString" _separator;
@"NSObject" _object;
@"NSMutableString" _descriptionString;
```

## Properties

```
@property (T@"NSObject",N,V_object) object;
@property (T@"NSMutableString",&,N,V_descriptionString) descriptionString;
@property (T@"NSString",C,N,V_separator) separator;
@property (T@"NSString",R,N) string;
```

## Class methods

```
+[UIDescriptionBuilder descriptionBuilderWithObject:];
+[UIDescriptionBuilder descriptionForObject:keys:];
+[UIDescriptionBuilder descriptionForObject:namesAndObjects:];
```

## Instance methods

```
-[UIDescriptionBuilder separator];
-[UIDescriptionBuilder descriptionString];
-[UIDescriptionBuilder setSeparator:];
-[UIDescriptionBuilder initWithObject:];
-[UIDescriptionBuilder appendName:doubleValue:];
-[UIDescriptionBuilder appendName:integerValue:];
-[UIDescriptionBuilder appendName:selector:];
-[UIDescriptionBuilder appendKeys:];
-[UIDescriptionBuilder appendKey:];
-[UIDescriptionBuilder appendName:pointerValue:];
-[UIDescriptionBuilder setObject:];
-[UIDescriptionBuilder tryAppendKey:];
-[UIDescriptionBuilder string];
-[UIDescriptionBuilder appendObject:withName:];
-[UIDescriptionBuilder setDescriptionString:];
-[UIDescriptionBuilder appendName:boolValue:];
-[UIDescriptionBuilder appendName:object:];
-[UIDescriptionBuilder appendName:intValue:];
-[UIDescriptionBuilder appendNamesAndObjects:];
-[UIDescriptionBuilder appendName:object:usingLightweightDescription:];
-[UIDescriptionBuilder appendName:unsignedInteger:];
-[UIDescriptionBuilder object];
```
