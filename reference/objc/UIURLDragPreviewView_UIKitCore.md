# `UIURLDragPreviewView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 3 properties, 8 instance methods, 7 class methods

## Instance variables

```
@"UILabel" _titleLabel;
@"UILabel" _urlLabel;
@"NSArray" _titleAndUrlConstraints;
@"NSArray" _urlOnlyConstraints;
@"NSString" _title;
@"NSURL" _url;
@"NSString" _urlText;
```

## Properties

```
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSURL",C,N,V_url) url;
@property (T@"NSString",C,N,V_urlText) urlText;
```

## Class methods

```
+[UIURLDragPreviewView initialize];
+[UIURLDragPreviewView _titleFont];
+[UIURLDragPreviewView _urlFont];
+[UIURLDragPreviewView viewWithTitle:URL:];
+[UIURLDragPreviewView viewWithTitle:URLText:];
+[UIURLDragPreviewView viewWithURL:];
+[UIURLDragPreviewView viewWithURLText:];
```

## Instance methods

```
-[UIURLDragPreviewView title];
-[UIURLDragPreviewView updateConstraints];
-[UIURLDragPreviewView setTitle:];
-[UIURLDragPreviewView setUrl:];
-[UIURLDragPreviewView initWithFrame:];
-[UIURLDragPreviewView url];
-[UIURLDragPreviewView urlText];
-[UIURLDragPreviewView setUrlText:];
```
