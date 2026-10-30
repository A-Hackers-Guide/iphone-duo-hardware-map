# `_UIDatePickerComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 9 instance methods, 2 class methods

## Instance variables

```
Q _equivalentUnit;
@"NSString" _formatString;
Q _calendarUnit;
d _width;
{_NSRange="location"Q"length"Q} _unitRange;
```

## Properties

```
@property (T@"NSString",R,N,V_formatString) formatString;
@property (TQ,R,N,V_calendarUnit) calendarUnit;
@property (TQ,R,N) equivalentUnit;
@property (T{_NSRange=QQ},N,V_unitRange) unitRange;
@property (Td,N,V_width) width;
```

## Class methods

```
+[_UIDatePickerComponent componentsFromDateFormatString:locale:followsSystemHourCycle:];
+[_UIDatePickerComponent componentsFromDateFormatString:locale:followsSystemHourCycle:desiredUnits:];
```

## Instance methods

```
-[_UIDatePickerComponent formatString];
-[_UIDatePickerComponent description];
-[_UIDatePickerComponent setWidth:];
-[_UIDatePickerComponent width];
-[_UIDatePickerComponent _initWithFormatString:calendarUnit:];
-[_UIDatePickerComponent calendarUnit];
-[_UIDatePickerComponent equivalentUnit];
-[_UIDatePickerComponent setUnitRange:];
-[_UIDatePickerComponent unitRange];
```
