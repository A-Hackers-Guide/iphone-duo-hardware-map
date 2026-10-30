# `CLLocationButtonDrawing`

- Image: [`/System/Library/Frameworks/CoreLocationUI.framework/CoreLocationUI`](../userland/System__Library__Frameworks__CoreLocationUI.framework__CoreLocationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISDrawing`
- 9 instance variables, 12 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"CLLocationButtonTag" _currentTag;
@"UISSlotStyle" _style;
B _remote;
I _secureName;
@"NSString" _localizedTitle;
@"UISTextLineDrawing" _textDrawing;
@"UISVectorGlyphDrawing" _glyphDrawing;
{CGSize="width"d"height"d} _neededSize;
{CGSize="width"d"height"d} _engravedSize;
```

## Properties

```
@property (T{CGSize=dd},N,V_engravedSize) engravedSize;
@property (T{CGSize=dd},N,V_neededSize) neededSize;
@property (T@"NSString",&,N,V_localizedTitle) localizedTitle;
@property (T@"UISTextLineDrawing",&,N,V_textDrawing) textDrawing;
@property (T@"UISVectorGlyphDrawing",&,N,V_glyphDrawing) glyphDrawing;
@property (TI,R,N,V_secureName) secureName;
@property (T{CGSize=dd},R,N) drawingSize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) alignmentRect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CLLocationButtonDrawing _drawingWithStyle:tag:remote:];
```

## Instance methods

```
-[CLLocationButtonDrawing localizedTitle];
-[CLLocationButtonDrawing secureName];
-[CLLocationButtonDrawing setLocalizedTitle:];
-[CLLocationButtonDrawing drawInContext:atPoint:];
-[CLLocationButtonDrawing drawingSize];
-[CLLocationButtonDrawing imageWithStyle:tag:forRemote:];
-[CLLocationButtonDrawing setTextDrawing:];
-[CLLocationButtonDrawing _computeImageMetrics];
-[CLLocationButtonDrawing buttonPadding];
-[CLLocationButtonDrawing engravedSize];
-[CLLocationButtonDrawing glyphDrawing];
-[CLLocationButtonDrawing initWithStyle:tag:remote:];
-[CLLocationButtonDrawing neededSize];
-[CLLocationButtonDrawing setEngravedSize:];
-[CLLocationButtonDrawing setGlyphDrawing:];
-[CLLocationButtonDrawing setNeededSize:];
-[CLLocationButtonDrawing textDrawing];
```
