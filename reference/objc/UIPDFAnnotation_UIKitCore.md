# `UIPDFAnnotation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CALayerDelegate`
- 19 instance variables, 17 properties, 52 instance methods, 1 class methods

## Instance variables

```
^{CGPDFDictionary=} _dictionary;
^{CGColor=} _color;
^v _appearanceStream;
^{CGPDFString=} _pdfContents;
@"NSString" _annotationID;
B _hidden;
@"UIPDFAnnotationView" _annotationView;
@"UIPDFAnnotationController" _annotationController;
@"NSMutableArray" _quadPoints;
@"CALayer" _drawingLayer;
@"UIPDFSelection" _selection;
B editable;
@ data;
@"NSString" _contents;
q _index;
@"UIPDFPopupAnnotation" _popup;
@"NSString" _associatedAnnotationID;
@"UIPDFPage" _page;
Q _tag;
```

## Properties

```
@property (T@"CALayer",&,N,V_drawingLayer) drawingLayer;
@property (T@"UIPDFAnnotationView",&,N,V_annotationView) annotationView;
@property (T@"UIPDFPage",N,V_page) page;
@property (T@"UIPDFAnnotationController",N,V_annotationController) annotationController;
@property (TB,R,D,N) recognizeGestures;
@property (TB,N,Veditable) editable;
@property (T@"UIPDFSelection",D,N) selection;
@property (T@,&,N,Vdata) data;
@property (T@"NSString",&,N,V_contents) contents;
@property (Tq,N,V_index) index;
@property (T@"UIPDFPopupAnnotation",N,V_popup) popup;
@property (T@"NSString",&,N,V_associatedAnnotationID) associatedAnnotationID;
@property (TQ,N,V_tag) tag;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPDFAnnotation newAnnotationWithPage:fromArchive:];
```

## Instance methods

```
-[UIPDFAnnotation selection];
-[UIPDFAnnotation setSelection:];
-[UIPDFAnnotation setColor:];
-[UIPDFAnnotation drawInContext:];
-[UIPDFAnnotation setContents:];
-[UIPDFAnnotation archive];
-[UIPDFAnnotation contents];
-[UIPDFAnnotation init];
-[UIPDFAnnotation setTag:];
-[UIPDFAnnotation data];
-[UIPDFAnnotation dealloc];
-[UIPDFAnnotation annotationView];
-[UIPDFAnnotation drawLayer:inContext:];
-[UIPDFAnnotation setPage:];
-[UIPDFAnnotation index];
-[UIPDFAnnotation setIndex:];
-[UIPDFAnnotation color];
-[UIPDFAnnotation setData:];
-[UIPDFAnnotation page];
-[UIPDFAnnotation tag];
-[UIPDFAnnotation setEditable:];
-[UIPDFAnnotation bounds];
-[UIPDFAnnotation setAnnotationController:];
-[UIPDFAnnotation setAnnotationView:];
-[UIPDFAnnotation annotationController];
-[UIPDFAnnotation frame];
-[UIPDFAnnotation containsPoint:];
-[UIPDFAnnotation hidden];
-[UIPDFAnnotation descriptionHOLD];
-[UIPDFAnnotation Rect];
-[UIPDFAnnotation rectIn:];
-[UIPDFAnnotation annotationID];
-[UIPDFAnnotation annotationType];
-[UIPDFAnnotation associatedAnnotationID];
-[UIPDFAnnotation drawingLayer];
-[UIPDFAnnotation editable];
-[UIPDFAnnotation getImageNamed:ofType:];
-[UIPDFAnnotation hasPopUp];
-[UIPDFAnnotation initWithAnnotationDictionary:];
-[UIPDFAnnotation makeQuadpointsFrom:];
-[UIPDFAnnotation newPathFromQuadPoints];
-[UIPDFAnnotation newSelection];
-[UIPDFAnnotation pdfContents];
-[UIPDFAnnotation popUpAnnotationRect];
-[UIPDFAnnotation popup];
-[UIPDFAnnotation recognizeGestures];
-[UIPDFAnnotation setAnnotationID:];
-[UIPDFAnnotation setAssociatedAnnotationID:];
-[UIPDFAnnotation setDrawingLayer:];
-[UIPDFAnnotation setPageView:];
-[UIPDFAnnotation setPopup:];
-[UIPDFAnnotation viewClass];
```
