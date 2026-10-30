# `CDLabelProvider`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"CLKTextProvider" _textProvider;
@"CLKImageProvider" _imageProvider;
```

## Properties

```
@property (T@"CLKTextProvider",R,N,V_textProvider) textProvider;
@property (T@"CLKImageProvider",R,N,V_imageProvider) imageProvider;
```

## Class methods

```
+[CDLabelProvider supportsSecureCoding];
```

## Instance methods

```
-[CDLabelProvider textProvider];
-[CDLabelProvider imageProvider];
-[CDLabelProvider encodeWithCoder:];
-[CDLabelProvider initWithCoder:];
-[CDLabelProvider initWithTextProvider:imageProvider:];
```
