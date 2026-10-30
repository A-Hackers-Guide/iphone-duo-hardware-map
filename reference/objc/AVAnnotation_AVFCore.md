# `AVAnnotation`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 8 properties, 24 instance methods, 2 class methods

## Instance variables

```
@"NSString" _version;
@"NSUUID" _identifier;
@"NSString" _author;
@"NSDate" _lastModifiedDate;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _timeRange;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _normalizedBoundingBox;
q _zOrder;
@"NSArray" _representations;
```

## Properties

```
@property (T@"NSString",C,N,G_version,S_setVersion:) version;
@property (T@"NSUUID",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_author) author;
@property (T@"NSDate",C,N,V_lastModifiedDate) lastModifiedDate;
@property (T{?={?=qiIq}{?=qiIq}},N,V_timeRange) timeRange;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_normalizedBoundingBox) normalizedBoundingBox;
@property (Tq,N,V_zOrder) zOrder;
@property (T@"NSArray",C,N,V_representations) representations;
```

## Class methods

```
+[AVAnnotation initialize];
+[AVAnnotation annotationPropertyListToNonDataBindingsArray:];
```

## Instance methods

```
-[AVAnnotation setTimeRange:];
-[AVAnnotation setAuthor:];
-[AVAnnotation timeRange];
-[AVAnnotation author];
-[AVAnnotation identifier];
-[AVAnnotation lastModifiedDate];
-[AVAnnotation dealloc];
-[AVAnnotation setLastModifiedDate:];
-[AVAnnotation representations];
-[AVAnnotation setIdentifier:];
-[AVAnnotation hash];
-[AVAnnotation _setVersion:];
-[AVAnnotation _version];
-[AVAnnotation description];
-[AVAnnotation copyWithZone:];
-[AVAnnotation isEqual:];
-[AVAnnotation setZOrder:];
-[AVAnnotation zOrder];
-[AVAnnotation setRepresentations:];
-[AVAnnotation getJSONData:representationBinaryDataBindings:];
-[AVAnnotation initWithJSONData:representationBinaryDataBindings:error:];
-[AVAnnotation initWithTimeRange:normalizedBoundingBox:];
-[AVAnnotation normalizedBoundingBox];
-[AVAnnotation setNormalizedBoundingBox:];
```
