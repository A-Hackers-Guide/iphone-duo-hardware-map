# `HIDLibElement`

- Image: [`/System/Library/PrivateFrameworks/HID.framework/HID`](../userland/System__Library__PrivateFrameworks__HID.framework__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 22 properties, 36 instance methods, 2 class methods

## Instance variables

```
^{__IOHIDElement=} _element;
^{__IOHIDValue=} _defaultValue;
@"NSString" _psKey;
{IOHIDElementStruct="cookieMin"I"cookieMax"I"parentCookie"I"type"I"collectionType"I"flags"I"usagePage"I"usageMin"I"usageMax"I"min"i"max"i"scaledMin"i"scaledMax"i"size"I"reportSize"I"reportCount"I"reportID"I"unit"I"unitExponent"I"duplicateValueSize"I"duplicateIndex"I"bytes"I"valueSize"I"rawReportCount"I} _elementStruct;
B _isConstant;
B _isUpdated;
```

## Properties

```
@property (T^{__IOHIDElement=},V_element) elementRef;
@property (T^{__IOHIDValue=}) valueRef;
@property (T^{__IOHIDValue=},V_defaultValue) defaultValueRef;
@property (Tq) integerValue;
@property (T@"NSData") dataValue;
@property (T@"NSString",C,V_psKey) psKey;
@property (TQ,R) timestamp;
@property (Tq,R) length;
@property (T{IOHIDElementStruct=IIIIIIIIIiiiiIIIIIIIIIII},R,V_elementStruct) elementStruct;
@property (TB,V_isConstant) isConstant;
@property (TB,V_isUpdated) isUpdated;
@property (TI,R) elementCookie;
@property (TI,R) collectionCookie;
@property (Ti,R) type;
@property (TI,R) usage;
@property (TI,R) usagePage;
@property (TI,R) unit;
@property (TC,R) unitExponent;
@property (TC,R) reportID;
@property (TI,R) usageMin;
@property (TI,R) usageMax;
@property (Ti,R) collectionType;
```

## Class methods

```
+[HIDLibElement withElementRef:];
+[HIDLibElement withElementStruct:parent:index:];
```

## Instance methods

```
-[HIDLibElement usage];
-[HIDLibElement collectionType];
-[HIDLibElement isUpdated];
-[HIDLibElement dataValue];
-[HIDLibElement unit];
-[HIDLibElement setDataValue:];
-[HIDLibElement integerValue];
-[HIDLibElement unitExponent];
-[HIDLibElement dealloc];
-[HIDLibElement timestamp];
-[HIDLibElement length];
-[HIDLibElement isConstant];
-[HIDLibElement usagePage];
-[HIDLibElement type];
-[HIDLibElement description];
-[HIDLibElement setIntegerValue:];
-[HIDLibElement isEqual:];
-[HIDLibElement reportID];
-[HIDLibElement elementRef];
-[HIDLibElement valueRef];
-[HIDLibElement elementCookie];
-[HIDLibElement initWithElementRef:];
-[HIDLibElement psKey];
-[HIDLibElement setIsConstant:];
-[HIDLibElement setIsUpdated:];
-[HIDLibElement setPsKey:];
-[HIDLibElement setValueRef:];
-[HIDLibElement defaultValueRef];
-[HIDLibElement collectionCookie];
-[HIDLibElement elementStruct];
-[HIDLibElement initWithElementStruct:parent:index:];
-[HIDLibElement isEqualToHIDLibElement:];
-[HIDLibElement setDefaultValueRef:];
-[HIDLibElement setElementRef:];
-[HIDLibElement usageMax];
-[HIDLibElement usageMin];
```
