# `UIGraphicsPDFRendererContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGraphicsRendererContext`
- 3 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _inPage;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _documentBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _pageBounds;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_documentBounds) documentBounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_pageBounds) pageBounds;
@property (TB,V_inPage) inPage;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) pdfContextBounds;
```

## Instance methods

```
-[UIGraphicsPDFRendererContext pageBounds];
-[UIGraphicsPDFRendererContext setPageBounds:];
-[UIGraphicsPDFRendererContext addDestinationWithName:atPoint:];
-[UIGraphicsPDFRendererContext setDestinationWithName:forRect:];
-[UIGraphicsPDFRendererContext setURL:forRect:];
-[UIGraphicsPDFRendererContext beginPage];
-[UIGraphicsPDFRendererContext beginPageWithBounds:pageInfo:];
-[UIGraphicsPDFRendererContext documentBounds];
-[UIGraphicsPDFRendererContext inPage];
-[UIGraphicsPDFRendererContext pdfContextBounds];
-[UIGraphicsPDFRendererContext setDocumentBounds:];
-[UIGraphicsPDFRendererContext setInPage:];
-[UIGraphicsPDFRendererContext updateAuxInfo:];
```
