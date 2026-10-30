# `MLImageSize`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _pixelsWide;
q _pixelsHigh;
```

## Properties

```
@property (Tq,R,V_pixelsWide) pixelsWide;
@property (Tq,R,V_pixelsHigh) pixelsHigh;
```

## Class methods

```
+[MLImageSize supportsSecureCoding];
```

## Instance methods

```
-[MLImageSize encodeWithCoder:];
-[MLImageSize hash];
-[MLImageSize description];
-[MLImageSize initWithCoder:];
-[MLImageSize isEqual:];
-[MLImageSize initWithPixelsWide:pixelsHigh:];
-[MLImageSize isEqualToImageSize:];
-[MLImageSize pixelsHigh];
-[MLImageSize pixelsWide];
```
