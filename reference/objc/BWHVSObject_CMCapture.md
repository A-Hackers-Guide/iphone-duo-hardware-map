# `BWHVSObject`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 12 instance methods, 1 class methods

## Instance variables

```
i _groupID;
i _confidence;
f _laplacianVariance;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundingBox;
{?="width"i"height"i} _imageDimensions;
```

## Properties

```
@property (Ti,N,V_groupID) groupID;
@property (Ti,N,V_confidence) confidence;
@property (Tf,N,V_laplacianVariance) laplacianVariance;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_boundingBox) boundingBox;
@property (T{?=ii},N,V_imageDimensions) imageDimensions;
@property (T@"NSDictionary",R) metadataRepresentation;
```

## Class methods

```
+[BWHVSObject initialize];
```

## Instance methods

```
-[BWHVSObject setGroupID:];
-[BWHVSObject groupID];
-[BWHVSObject setBoundingBox:];
-[BWHVSObject boundingBox];
-[BWHVSObject setConfidence:];
-[BWHVSObject imageDimensions];
-[BWHVSObject setImageDimensions:];
-[BWHVSObject confidence];
-[BWHVSObject initWithANSTObject:imageDimensions:];
-[BWHVSObject laplacianVariance];
-[BWHVSObject metadataRepresentation];
-[BWHVSObject setLaplacianVariance:];
```
