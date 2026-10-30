# `TULabeledHandle`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _isSuggested;
@"TUHandle" _handle;
@"NSString" _label;
```

## Properties

```
@property (T@"TUHandle",R,N,V_handle) handle;
@property (T@"NSString",R,C,N,V_label) label;
@property (TB,R,N,V_isSuggested) isSuggested;
```

## Class methods

```
+[TULabeledHandle supportsSecureCoding];
```

## Instance methods

```
-[TULabeledHandle isSuggested];
-[TULabeledHandle init];
-[TULabeledHandle label];
-[TULabeledHandle handle];
-[TULabeledHandle encodeWithCoder:];
-[TULabeledHandle hash];
-[TULabeledHandle description];
-[TULabeledHandle initWithCoder:];
-[TULabeledHandle copyWithZone:];
-[TULabeledHandle isEqual:];
-[TULabeledHandle initWithHandle:label:isSuggested:];
-[TULabeledHandle isEqualToLabeledHandle:];
```
