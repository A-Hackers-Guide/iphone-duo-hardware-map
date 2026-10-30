# `SBFCARendererImageRepresentation`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 8 instance methods, 5 class methods

## Instance variables

```
q _representationType;
@"NSURL" _fileURL;
@"NSData" _imageData;
q _imageOrientation;
@"IOSurface" _surface;
```

## Properties

```
@property (Tq,R,N,V_representationType) representationType;
@property (T@"NSURL",R,C,N,V_fileURL) fileURL;
@property (T@"NSData",R,C,N,V_imageData) imageData;
@property (Tq,R,N,V_imageOrientation) imageOrientation;
@property (T@"IOSurface",R,N,V_surface) surface;
```

## Class methods

```
+[SBFCARendererImageRepresentation supportsSecureCoding];
+[SBFCARendererImageRepresentation representationWithFileURL:imageOrientation:];
+[SBFCARendererImageRepresentation representationWithIOSurface:imageOrientation:];
+[SBFCARendererImageRepresentation representationWithImage:];
+[SBFCARendererImageRepresentation representationWithImageData:imageOrientation:];
```

## Instance methods

```
-[SBFCARendererImageRepresentation surface];
-[SBFCARendererImageRepresentation fileURL];
-[SBFCARendererImageRepresentation imageData];
-[SBFCARendererImageRepresentation imageOrientation];
-[SBFCARendererImageRepresentation encodeWithCoder:];
-[SBFCARendererImageRepresentation initWithCoder:];
-[SBFCARendererImageRepresentation representationType];
-[SBFCARendererImageRepresentation createCGImageReturningScale:];
```
