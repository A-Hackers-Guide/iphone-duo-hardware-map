# `BKDisplayAnnotation`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 28 instance methods, 5 class methods

## Instance variables

```
@"BKDisplayAnnotationLocation" _location;
@"BKDisplayAnnotationRenderer" _renderer;
@"NSString" _section;
q _subnodeScreenEdgeTreatment;
@"<BKDisplayAnnotationContent>" _content;
@"BKDisplayAnnotationController" _annotationController;
@"BKDisplayAnnotationStyleSheet" _styleSheet;
@"BKNamespaceNode" _namespaceNode;
```

## Properties

```
@property (T@"<BKDisplayAnnotationContent>",&,N,V_content) content;
@property (T@"BKDisplayAnnotationController",W,N,V_annotationController) annotationController;
@property (T@"BKDisplayAnnotationStyleSheet",&,N,V_styleSheet) styleSheet;
@property (T@"BKNamespaceNode",W,N,V_namespaceNode) namespaceNode;
@property (T@"BKDisplayAnnotationLocation",&,N,V_location) location;
@property (T@"BKDisplayAnnotationRenderer",&,N,V_renderer) renderer;
@property (T@"NSString",C,N,V_section) section;
@property (Tq,N,V_subnodeScreenEdgeTreatment) subnodeScreenEdgeTreatment;
```

## Class methods

```
+[BKDisplayAnnotation new];
+[BKDisplayAnnotation annotationWithEllipseSize:displayRenderSpace:];
+[BKDisplayAnnotation annotationWithRectangleSize:displayRenderSpace:];
+[BKDisplayAnnotation annotationWithString:displayRenderSpace:];
+[BKDisplayAnnotation subannotationWithString:displayRenderSpace:];
```

## Instance methods

```
-[BKDisplayAnnotation setSection:];
-[BKDisplayAnnotation section];
-[BKDisplayAnnotation setContent:];
-[BKDisplayAnnotation renderer];
-[BKDisplayAnnotation succinctDescriptionBuilder];
-[BKDisplayAnnotation init];
-[BKDisplayAnnotation content];
-[BKDisplayAnnotation location];
-[BKDisplayAnnotation setString:];
-[BKDisplayAnnotation descriptionWithMultilinePrefix:];
-[BKDisplayAnnotation succinctDescription];
-[BKDisplayAnnotation setLocation:];
-[BKDisplayAnnotation setStyleSheet:];
-[BKDisplayAnnotation description];
-[BKDisplayAnnotation setRenderer:];
-[BKDisplayAnnotation setAnnotationController:];
-[BKDisplayAnnotation styleSheet];
-[BKDisplayAnnotation isEqual:];
-[BKDisplayAnnotation annotationController];
-[BKDisplayAnnotation descriptionBuilderWithMultilinePrefix:];
-[BKDisplayAnnotation _initWithDisplayRenderSpace:];
-[BKDisplayAnnotation modifyStyleSheet:];
-[BKDisplayAnnotation namespaceNode];
-[BKDisplayAnnotation setNamespaceNode:];
-[BKDisplayAnnotation setShapeSize:];
-[BKDisplayAnnotation setStyleModifier:];
-[BKDisplayAnnotation setSubnodeScreenEdgeTreatment:];
-[BKDisplayAnnotation subnodeScreenEdgeTreatment];
```
