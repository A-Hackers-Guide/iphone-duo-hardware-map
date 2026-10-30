# `_UIDebugReportFormatter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
Q _indentLevel;
@"NSString" _indentString;
Q _extraBodyIndentLevel;
```

## Properties

```
@property (TQ,N,V_indentLevel) indentLevel;
@property (T@"NSString",C,N,V_indentString) indentString;
@property (TQ,N,V_extraBodyIndentLevel) extraBodyIndentLevel;
```

## Class methods

```
+[_UIDebugReportFormatter defaultFormatter];
```

## Instance methods

```
-[_UIDebugReportFormatter init];
-[_UIDebugReportFormatter indentLevel];
-[_UIDebugReportFormatter setIndentLevel:];
-[_UIDebugReportFormatter extraBodyIndentLevel];
-[_UIDebugReportFormatter indentString];
-[_UIDebugReportFormatter setExtraBodyIndentLevel:];
-[_UIDebugReportFormatter setIndentString:];
-[_UIDebugReportFormatter stringFromReportComponents:];
```
