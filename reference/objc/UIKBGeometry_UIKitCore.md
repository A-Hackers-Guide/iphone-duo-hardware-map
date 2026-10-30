# `UIKBGeometry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`, `NSCopying`
- 11 instance variables, 11 properties, 39 instance methods, 5 class methods

## Instance variables

```
@"NSString" m_name;
{?="amount"d"unit"i} m_x;
{?="amount"d"unit"i} m_y;
{?="amount"d"unit"i} m_w;
{?="amount"d"unit"i} m_h;
{?="amount"d"unit"i} m_paddingTop;
{?="amount"d"unit"i} m_paddingLeft;
{?="amount"d"unit"i} m_paddingBottom;
{?="amount"d"unit"i} m_paddingRight;
B m_explicitlySpecified;
B m_isTemplate;
```

## Properties

```
@property (T@"NSString",&,N,Vm_name) name;
@property (T{?=di},N,SsetX:,Vm_x) x;
@property (T{?=di},N,SsetY:,Vm_y) y;
@property (T{?=di},N,SsetW:,Vm_w) w;
@property (T{?=di},N,SsetH:,Vm_h) h;
@property (T{?=di},N,SsetPaddingTop:,Vm_paddingTop) paddingTop;
@property (T{?=di},N,SsetPaddingLeft:,Vm_paddingLeft) paddingLeft;
@property (T{?=di},N,SsetPaddingBottom:,Vm_paddingBottom) paddingBottom;
@property (T{?=di},N,SsetPaddingRight:,Vm_paddingRight) paddingRight;
@property (TB,N,Vm_explicitlySpecified) explicitlySpecified;
@property (TB,N,Vm_isTemplate) isTemplate;
```

## Class methods

```
+[UIKBGeometry geometry];
+[UIKBGeometry codeStringForValue:];
+[UIKBGeometry geometryWithOriginValue:sizeValue:];
+[UIKBGeometry geometryWithRect:];
+[UIKBGeometry performOperations:withScale:];
```

## Instance methods

```
-[UIKBGeometry init];
-[UIKBGeometry y];
-[UIKBGeometry shortDescription];
-[UIKBGeometry setX:];
-[UIKBGeometry setY:];
-[UIKBGeometry x];
-[UIKBGeometry encodeWithCoder:];
-[UIKBGeometry hash];
-[UIKBGeometry description];
-[UIKBGeometry setName:];
-[UIKBGeometry initWithCoder:];
-[UIKBGeometry setIsTemplate:];
-[UIKBGeometry copyWithZone:];
-[UIKBGeometry isEqual:];
-[UIKBGeometry name];
-[UIKBGeometry isTemplate];
-[UIKBGeometry frame];
-[UIKBGeometry w];
-[UIKBGeometry h];
-[UIKBGeometry paddedFrameWithContainingFrame:];
-[UIKBGeometry setPaddingLeft:];
-[UIKBGeometry usesPercentages];
-[UIKBGeometry explicitlySpecified];
-[UIKBGeometry frameWithContainingFrame:];
-[UIKBGeometry initTemplateWithName:rect:padding:];
-[UIKBGeometry initWithName:rect:padding:];
-[UIKBGeometry overrideGeometry:];
-[UIKBGeometry paddedFrameWithResolvedFrame:];
-[UIKBGeometry paddingBottom];
-[UIKBGeometry paddingLeft];
-[UIKBGeometry paddingRight];
-[UIKBGeometry paddingTop];
-[UIKBGeometry setExplicitlySpecified:];
-[UIKBGeometry setH:];
-[UIKBGeometry setPaddingBottom:];
-[UIKBGeometry setPaddingRight:];
-[UIKBGeometry setPaddingTop:];
-[UIKBGeometry setW:];
-[UIKBGeometry usesAutomaticMetrics];
```
