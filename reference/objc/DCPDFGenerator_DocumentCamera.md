# `DCPDFGenerator`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
^{CGContext=} _pdfContext;
@"NSURL" _fileURL;
@"NSString" _title;
@"NSMutableData" _data;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _pageRect;
```

## Properties

```
@property (T@"NSURL",C,N,V_fileURL) fileURL;
@property (T@"NSString",C,N,V_title) title;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_pageRect) pageRect;
@property (T@"NSMutableData",&,N,V_data) data;
@property (T@"NSURL",R,N) url;
```

## Instance methods

```
-[DCPDFGenerator setFileURL:];
-[DCPDFGenerator fileURL];
-[DCPDFGenerator init];
-[DCPDFGenerator data];
-[DCPDFGenerator dealloc];
-[DCPDFGenerator title];
-[DCPDFGenerator setData:];
-[DCPDFGenerator setTitle:];
-[DCPDFGenerator url];
-[DCPDFGenerator startGenerating];
-[DCPDFGenerator addPageWithPageRect:renderBlock:];
-[DCPDFGenerator addPageWithRenderBlock:];
-[DCPDFGenerator finishGenerating];
-[DCPDFGenerator initWithMutableData:pageRect:title:];
-[DCPDFGenerator initWithURL:pageRect:title:];
-[DCPDFGenerator pageRect];
-[DCPDFGenerator setPageRect:];
```
