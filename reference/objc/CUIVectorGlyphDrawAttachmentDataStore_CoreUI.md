# `CUIVectorGlyphDrawAttachmentDataStore`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSData" _data;
@"CUIVectorGlyphManagedPointArray" _anchors;
```

## Properties

```
@property (T@"NSData",R,&,N,V_data) data;
@property (T@"CUIVectorGlyphManagedPointArray",R,&,N,V_anchors) anchors;
@property (TQ,R,N) count;
```

## Class methods

```
+[CUIVectorGlyphDrawAttachmentDataStore _customDataAtom];
```

## Instance methods

```
-[CUIVectorGlyphDrawAttachmentDataStore dataAtIndex:];
-[CUIVectorGlyphDrawAttachmentDataStore initAdoptingData:anchors:];
-[CUIVectorGlyphDrawAttachmentDataStore copyApplyingScaleFactor:];
-[CUIVectorGlyphDrawAttachmentDataStore init];
-[CUIVectorGlyphDrawAttachmentDataStore data];
-[CUIVectorGlyphDrawAttachmentDataStore dealloc];
-[CUIVectorGlyphDrawAttachmentDataStore count];
-[CUIVectorGlyphDrawAttachmentDataStore anchors];
-[CUIVectorGlyphDrawAttachmentDataStore initWithSVGNode:];
-[CUIVectorGlyphDrawAttachmentDataStore computeNumEntries:withScanner:fieldDelimiter:];
-[CUIVectorGlyphDrawAttachmentDataStore initWithSVGString:];
-[CUIVectorGlyphDrawAttachmentDataStore encodeToSVGNode:];
-[CUIVectorGlyphDrawAttachmentDataStore createSVGString];
-[CUIVectorGlyphDrawAttachmentDataStore copyWithZone:];
```
