# `CUIVectorGlyphLayerDrawAttachmentStore`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSData" _data;
r^^{CUIVectorGlyphLayerDrawAttachment} _attachments;
Q _count;
```

## Properties

```
@property (Tr^^{CUIVectorGlyphLayerDrawAttachment},R,N,V_attachments) attachments;
@property (TQ,R,N,V_count) count;
```

## Instance methods

```
-[CUIVectorGlyphLayerDrawAttachmentStore init];
-[CUIVectorGlyphLayerDrawAttachmentStore dealloc];
-[CUIVectorGlyphLayerDrawAttachmentStore count];
-[CUIVectorGlyphLayerDrawAttachmentStore attachments];
-[CUIVectorGlyphLayerDrawAttachmentStore initFromSVGString:attachmentData:];
-[CUIVectorGlyphLayerDrawAttachmentStore _setupEmpty];
-[CUIVectorGlyphLayerDrawAttachmentStore computeCapacity:numAttachments:withScanner:usingAttachmentDelimiter:fieldDelimiter:digits:];
```
