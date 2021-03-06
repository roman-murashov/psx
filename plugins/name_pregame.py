from ida_name import set_name
from base_types import Ident

funcs = [
	# diabpsx/psxsrc/pregame.cpp
	Ident(addr=0x80139BFC, name="PreGameOnlyTestRoutine__Fv", decl="void PreGameOnlyTestRoutine__Fv()"),

	# diabpsx/source/drlg_l1.cpp
	Ident(addr=0x8013BCB0, name="DRLG_PlaceDoor__Fii", decl="void DRLG_PlaceDoor__Fii(int x, int y)"),
	Ident(addr=0x8013C190, name="DRLG_L1Shadows__Fv", decl="void DRLG_L1Shadows__Fv()"),
	Ident(addr=0x8013C5A0, name="DRLG_PlaceMiniSet__FPCUciiiiiii", decl="int DRLG_PlaceMiniSet__FPCUciiiiiii(unsigned char *miniset, int tmin, int tmax, int cx, int cy, int setview, int noquad, int ldir)"),
	Ident(addr=0x8013CA08, name="DRLG_SetWalls__Fv", decl="void DRLG_SetWalls__Fv()"),
	Ident(addr=0x8013CAC4, name="DRLG_L1Floor__Fv", decl="void DRLG_L1Floor__Fv()"),
	Ident(addr=0x8013CBA8, name="DRLG_L1Pass3__Fv", decl="void DRLG_L1Pass3__Fv()"),
	Ident(addr=0x8013CDA0, name="DRLG_LoadL1SP__Fv", decl="void DRLG_LoadL1SP__Fv()"),
	Ident(addr=0x8013CE7C, name="DRLG_FreeL1SP__Fv", decl="void DRLG_FreeL1SP__Fv()"),
	Ident(addr=0x8013CEAC, name="DRLG_Init_Globals__Fv", decl="void DRLG_Init_Globals__Fv()"),
	Ident(addr=0x8013CECC, name="set_restore_lighting__Fv", decl="void set_restore_lighting__Fv()"),
	Ident(addr=0x8013CF5C, name="DRLG_InitL1Vals__Fv", decl="void DRLG_InitL1Vals__Fv()"),
	Ident(addr=0x8013CF64, name="LoadL1Dungeon__FPcii", decl="void LoadL1Dungeon__FPcii(char *sFileName, int vx, int vy)"),
	Ident(addr=0x8013D138, name="LoadPreL1Dungeon__FPcii", decl="void LoadPreL1Dungeon__FPcii(char *sFileName, int vx, int vy)"),
	Ident(addr=0x8013D2F8, name="InitL5Dungeon__Fv", decl="void InitL5Dungeon__Fv()"),
	Ident(addr=0x8013D37C, name="L5ClearFlags__Fv", decl="void L5ClearFlags__Fv()"),
	Ident(addr=0x8013D3CC, name="L5drawRoom__Fiiii", decl="void L5drawRoom__Fiiii(int x, int y, int w, int h)"),
	Ident(addr=0x8013D438, name="L5checkRoom__Fiiii", decl="unsigned char L5checkRoom__Fiiii(int x, int y, int width, int height)"),
	Ident(addr=0x8013D4CC, name="L5roomGen__Fiiiii", decl="void L5roomGen__Fiiiii(int x, int y, int w, int h, int dir)"),
	Ident(addr=0x8013D7FC, name="L5firstRoom__Fv", decl="void L5firstRoom__Fv()"),
	Ident(addr=0x8013DB9C, name="L5GetArea__Fv", decl="long L5GetArea__Fv()"),
	Ident(addr=0x8013DBFC, name="L5makeDungeon__Fv", decl="void L5makeDungeon__Fv()"),
	Ident(addr=0x8013DC88, name="L5makeDmt__Fv", decl="void L5makeDmt__Fv()"),
	Ident(addr=0x8013DD70, name="L5HWallOk__Fii", decl="int L5HWallOk__Fii(int i, int j)"),
	Ident(addr=0x8013DEAC, name="L5VWallOk__Fii", decl="int L5VWallOk__Fii(int i, int j)"),
	Ident(addr=0x8013DFF4, name="L5HorizWall__Fiici", decl="void L5HorizWall__Fiici(int i, int j, char p, int dx)"),
	Ident(addr=0x8013E22C, name="L5VertWall__Fiici", decl="void L5VertWall__Fiici(int i, int j, char p, int dy)"),
	Ident(addr=0x8013E458, name="L5AddWall__Fv", decl="void L5AddWall__Fv()"),
	Ident(addr=0x8013E6B4, name="DRLG_L5GChamber__Fiiiiii", decl="void DRLG_L5GChamber__Fiiiiii(int sx, int sy, int topflag, int bottomflag, int leftflag, int rightflag)"),
	Ident(addr=0x8013E974, name="DRLG_L5GHall__Fiiii", decl="void DRLG_L5GHall__Fiiii(int x1, int y1, int x2, int y2)"),
	Ident(addr=0x8013EA28, name="L5tileFix__Fv", decl="void L5tileFix__Fv()"),
	Ident(addr=0x8013F2EC, name="DRLG_L5Subs__Fv", decl="void DRLG_L5Subs__Fv()"),
	Ident(addr=0x8013F4F8, name="DRLG_L5SetRoom__Fii", decl="void DRLG_L5SetRoom__Fii(int rx1, int ry1)"),
	Ident(addr=0x8013F5F8, name="L5FillChambers__Fv", decl="void L5FillChambers__Fv()"),
	Ident(addr=0x8013FCE4, name="DRLG_L5FTVR__Fiiiii", decl="void DRLG_L5FTVR__Fiiiii(int i, int j, int x, int y, int d)"),
	Ident(addr=0x8014016C, name="DRLG_L5FloodTVal__Fv", decl="void DRLG_L5FloodTVal__Fv()"),
	Ident(addr=0x80140264, name="DRLG_L5TransFix__Fv", decl="void DRLG_L5TransFix__Fv()"),
	Ident(addr=0x801406A8, name="DRLG_L5DirtFix__Fv", decl="void DRLG_L5DirtFix__Fv()"),
	Ident(addr=0x80140824, name="DRLG_L5CornerFix__Fv", decl="void DRLG_L5CornerFix__Fv()"),
	Ident(addr=0x80140930, name="DRLG_L5__Fi", decl="void DRLG_L5__Fi(int entry)"),
	Ident(addr=0x80140E64, name="CreateL5Dungeon__FUii", decl="void CreateL5Dungeon__FUii(unsigned int rseed, int entry)"),

	# diabpsx/source/drlg_l2.cpp
	Ident(addr=0x80143408, name="DRLG_L2PlaceMiniSet__FPUciiiiii", decl="unsigned char DRLG_L2PlaceMiniSet__FPUciiiiii(unsigned char *miniset, int tmin, int tmax, int cx, int cy, int setview, int ldir)"),
	Ident(addr=0x80143798, name="DRLG_L2PlaceRndSet__FPUci", decl="void DRLG_L2PlaceRndSet__FPUci(unsigned char *miniset, int rndper)"),
	Ident(addr=0x80143A90, name="DRLG_L2Subs__Fv", decl="void DRLG_L2Subs__Fv()"),
	Ident(addr=0x80143C80, name="DRLG_L2Shadows__Fv", decl="void DRLG_L2Shadows__Fv()"),
	Ident(addr=0x80143E44, name="InitDungeon__Fv", decl="void InitDungeon__Fv()"),
	Ident(addr=0x80143E8C, name="DRLG_LoadL2SP__Fv", decl="void DRLG_LoadL2SP__Fv()"),
	Ident(addr=0x80143F2C, name="DRLG_FreeL2SP__Fv", decl="void DRLG_FreeL2SP__Fv()"),
	Ident(addr=0x80143F5C, name="DRLG_L2SetRoom__Fii", decl="void DRLG_L2SetRoom__Fii(int rx1, int ry1)"),
	Ident(addr=0x8014405C, name="DefineRoom__Fiiiii", decl="void DefineRoom__Fiiiii(int nX1, int nY1, int nX2, int nY2, int ForceHW)"),
	Ident(addr=0x80144260, name="CreateDoorType__Fii", decl="void CreateDoorType__Fii(int nX, int nY)"),
	Ident(addr=0x80144344, name="PlaceHallExt__Fii", decl="void PlaceHallExt__Fii(int nX, int nY)"),
	Ident(addr=0x8014437C, name="AddHall__Fiiiii", decl="void AddHall__Fiiiii(int nX1, int nY1, int nX2, int nY2, int nHd)"),
	Ident(addr=0x80144454, name="CreateRoom__Fiiiiiiiii", decl="void CreateRoom__Fiiiiiiiii(int nX1, int nY1, int nX2, int nY2, int nRDest, int nHDir, int ForceHW, int nH, int nW)"),
	Ident(addr=0x80144AC4, name="GetHall__FPiN40", decl="void GetHall__FPiN40(int *nX1, int *nY1, int *nX2, int *nY2, int *nHd)"),
	Ident(addr=0x80144B5C, name="ConnectHall__Fiiiii", decl="void ConnectHall__Fiiiii(int nX1, int nY1, int nX2, int nY2, int nHd)"),
	Ident(addr=0x801451BC, name="DoPatternCheck__Fii", decl="void DoPatternCheck__Fii(int i, int j)"),
	Ident(addr=0x80145494, name="L2TileFix__Fv", decl="void L2TileFix__Fv()"),
	Ident(addr=0x801455B8, name="DL2_Cont__FUcUcUcUc", decl="unsigned char DL2_Cont__FUcUcUcUc(unsigned char x1f, unsigned char y1f, unsigned char x2f, unsigned char y2f)"),
	Ident(addr=0x80145638, name="DL2_NumNoChar__Fv", decl="int DL2_NumNoChar__Fv()"),
	Ident(addr=0x80145694, name="DL2_DrawRoom__Fiiii", decl="void DL2_DrawRoom__Fiiii(int x1, int y1, int x2, int y2)"),
	Ident(addr=0x80145798, name="DL2_KnockWalls__Fiiii", decl="void DL2_KnockWalls__Fiiii(int x1, int y1, int x2, int y2)"),
	Ident(addr=0x80145968, name="DL2_FillVoids__Fv", decl="unsigned char DL2_FillVoids__Fv()"),
	Ident(addr=0x801462E4, name="CreateDungeon__Fv", decl="unsigned char CreateDungeon__Fv()"),
	Ident(addr=0x801465F0, name="DRLG_L2Pass3__Fv", decl="void DRLG_L2Pass3__Fv()"),
	Ident(addr=0x801467E8, name="DRLG_L2FTVR__Fiiiii", decl="void DRLG_L2FTVR__Fiiiii(int i, int j, int x, int y, int d)"),
	Ident(addr=0x80146C70, name="DRLG_L2FloodTVal__Fv", decl="void DRLG_L2FloodTVal__Fv()"),
	Ident(addr=0x80146D68, name="DRLG_L2TransFix__Fv", decl="void DRLG_L2TransFix__Fv()"),
	Ident(addr=0x80146F94, name="L2DirtFix__Fv", decl="void L2DirtFix__Fv()"),
	Ident(addr=0x801470F4, name="L2LockoutFix__Fv", decl="void L2LockoutFix__Fv()"),
	Ident(addr=0x80147478, name="L2DoorFix__Fv", decl="void L2DoorFix__Fv()"),
	Ident(addr=0x80147528, name="DRLG_L2SetWalls__Fv", decl="void DRLG_L2SetWalls__Fv()"),
	Ident(addr=0x801476E0, name="DRLG_L2__Fi", decl="void DRLG_L2__Fi(int entry)"),
	Ident(addr=0x80148134, name="DRLG_InitL2Vals__Fv", decl="void DRLG_InitL2Vals__Fv()"),
	Ident(addr=0x8014813C, name="LoadL2Dungeon__FPcii", decl="void LoadL2Dungeon__FPcii(char *sFileName, int vx, int vy)"),
	Ident(addr=0x80148358, name="LoadPreL2Dungeon__FPcii", decl="void LoadPreL2Dungeon__FPcii(char *sFileName, int vx, int vy)"),
	Ident(addr=0x8014854C, name="CreateL2Dungeon__FUii", decl="void CreateL2Dungeon__FUii(unsigned int rseed, int entry)"),

	# diabpsx/source/drlg_l3.cpp
	Ident(addr=0x80148F98, name="InitL3Dungeon__Fv", decl="void InitL3Dungeon__Fv()"),
	Ident(addr=0x8014901C, name="SetBlankL3Dungeon__Fv", decl="void SetBlankL3Dungeon__Fv()"),
	Ident(addr=0x80149078, name="FixL3Dungeon__Fv", decl="void FixL3Dungeon__Fv()"),
	Ident(addr=0x801490EC, name="DRLG_L3FillRoom__Fiiii", decl="int DRLG_L3FillRoom__Fiiii(int x1, int y1, int x2, int y2)"),
	Ident(addr=0x8014933C, name="DRLG_L3CreateBlock__Fiiii", decl="void DRLG_L3CreateBlock__Fiiii(int x, int y, int obs, int dir)"),
	Ident(addr=0x801495BC, name="DRLG_L3FloorArea__Fiiii", decl="void DRLG_L3FloorArea__Fiiii(int x1, int y1, int x2, int y2)"),
	Ident(addr=0x80149624, name="DRLG_L3FillDiags__Fv", decl="void DRLG_L3FillDiags__Fv()"),
	Ident(addr=0x80149750, name="DRLG_L3FillSingles__Fv", decl="void DRLG_L3FillSingles__Fv()"),
	Ident(addr=0x8014981C, name="DRLG_L3FillStraights__Fv", decl="void DRLG_L3FillStraights__Fv()"),
	Ident(addr=0x80149BC8, name="DRLG_L3Edges__Fv", decl="void DRLG_L3Edges__Fv()"),
	Ident(addr=0x80149C08, name="DRLG_L3GetFloorArea__Fv", decl="int DRLG_L3GetFloorArea__Fv()"),
	Ident(addr=0x80149C58, name="DRLG_L3MakeMegas__Fv", decl="void DRLG_L3MakeMegas__Fv()"),
	Ident(addr=0x80149D94, name="DRLG_L3River__Fv", decl="void DRLG_L3River__Fv()"),
	Ident(addr=0x8014A7BC, name="DRLG_L3SpawnEdge__FiiPi", decl="int DRLG_L3SpawnEdge__FiiPi(int x, int y, int *totarea)"),
	Ident(addr=0x8014AA48, name="DRLG_L3Spawn__FiiPi", decl="int DRLG_L3Spawn__FiiPi(int x, int y, int *totarea)"),
	Ident(addr=0x8014AC54, name="DRLG_L3Pool__Fv", decl="void DRLG_L3Pool__Fv()"),
	Ident(addr=0x8014AEA4, name="DRLG_L3PoolFix__Fv", decl="void DRLG_L3PoolFix__Fv()"),
	Ident(addr=0x8014B0C4, name="DRLG_L3PlaceMiniSet__FPCUciiiiii", decl="int DRLG_L3PlaceMiniSet__FPCUciiiiii(unsigned char *miniset, int tmin, int tmax, int cx, int cy, int setview, int ldir)"),
	Ident(addr=0x8014B430, name="DRLG_L3PlaceRndSet__FPCUci", decl="void DRLG_L3PlaceRndSet__FPCUci(unsigned char *miniset, int rndper)"),
	Ident(addr=0x8014B76C, name="WoodVertU__Fii", decl="unsigned char WoodVertU__Fii(int i, int y)"),
	Ident(addr=0x8014B818, name="WoodVertD__Fii", decl="unsigned char WoodVertD__Fii(int i, int y)"),
	Ident(addr=0x8014B8B4, name="WoodHorizL__Fii", decl="unsigned char WoodHorizL__Fii(int x, int j)"),
	Ident(addr=0x8014B948, name="WoodHorizR__Fii", decl="unsigned char WoodHorizR__Fii(int x, int j)"),
	Ident(addr=0x8014B9CC, name="AddFenceDoors__Fv", decl="void AddFenceDoors__Fv()"),
	Ident(addr=0x8014BAB0, name="FenceDoorFix__Fv", decl="void FenceDoorFix__Fv()"),
	Ident(addr=0x8014BCA4, name="DRLG_L3Wood__Fv", decl="void DRLG_L3Wood__Fv()"),
	Ident(addr=0x8014C478, name="DRLG_L3Anvil__Fv", decl="int DRLG_L3Anvil__Fv()"),
	Ident(addr=0x8014C6D0, name="FixL3Warp__Fv", decl="void FixL3Warp__Fv()"),
	Ident(addr=0x8014C7B8, name="FixL3HallofHeroes__Fv", decl="void FixL3HallofHeroes__Fv()"),
	Ident(addr=0x8014C90C, name="DRLG_L3LockRec__Fii", decl="void DRLG_L3LockRec__Fii(int x, int y)"),
	Ident(addr=0x8014C9A8, name="DRLG_L3Lockout__Fv", decl="unsigned char DRLG_L3Lockout__Fv()"),
	Ident(addr=0x8014CA68, name="DRLG_L3SetWalls__Fv", decl="void DRLG_L3SetWalls__Fv()"),
	Ident(addr=0x8014CB1C, name="DRLG_L3__Fi", decl="void DRLG_L3__Fi(int entry)"),
	Ident(addr=0x8014D238, name="DRLG_L3Pass3__Fv", decl="void DRLG_L3Pass3__Fv()"),
	Ident(addr=0x8014D450, name="CreateL3Dungeon__FUii", decl="void CreateL3Dungeon__FUii(unsigned int rseed, int entry)"),
	Ident(addr=0x8014D4C8, name="LoadL3Dungeon__FPcii", decl="void LoadL3Dungeon__FPcii(char *sFileName, int vx, int vy)"),
	Ident(addr=0x8014D64C, name="LoadPreL3Dungeon__FPcii", decl="void LoadPreL3Dungeon__FPcii(char *sFileName, int vx, int vy)"),

	# diabpsx/source/drlg_l4.cpp
	Ident(addr=0x8014F4A8, name="DRLG_L4Shadows__Fv", decl="void DRLG_L4Shadows__Fv()"),
	Ident(addr=0x8014F56C, name="InitL4Dungeon__Fv", decl="void InitL4Dungeon__Fv()"),
	Ident(addr=0x8014F620, name="DRLG_LoadL4SP__Fv", decl="void DRLG_LoadL4SP__Fv()"),
	Ident(addr=0x8014F6C4, name="DRLG_FreeL4SP__Fv", decl="void DRLG_FreeL4SP__Fv()"),
	Ident(addr=0x8014F6F4, name="DRLG_L4SetSPRoom__Fii", decl="void DRLG_L4SetSPRoom__Fii(int rx1, int ry1)"),
	Ident(addr=0x8014F7F4, name="L4makeDmt__Fv", decl="void L4makeDmt__Fv()"),
	Ident(addr=0x8014F898, name="L4HWallOk__Fii", decl="int L4HWallOk__Fii(int i, int j)"),
	Ident(addr=0x8014F9E8, name="L4VWallOk__Fii", decl="int L4VWallOk__Fii(int i, int j)"),
	Ident(addr=0x8014FB58, name="L4HorizWall__Fiii", decl="void L4HorizWall__Fiii(int i, int j, int dx)"),
	Ident(addr=0x8014FD28, name="L4VertWall__Fiii", decl="void L4VertWall__Fiii(int i, int j, int dy)"),
	Ident(addr=0x8014FEEC, name="L4AddWall__Fv", decl="void L4AddWall__Fv()"),
	Ident(addr=0x80150394, name="L4tileFix__Fv", decl="void L4tileFix__Fv()"),
	Ident(addr=0x8015257C, name="DRLG_L4Subs__Fv", decl="void DRLG_L4Subs__Fv()"),
	Ident(addr=0x8015275C, name="L4makeDungeon__Fv", decl="void L4makeDungeon__Fv()"),
	Ident(addr=0x80152994, name="uShape__Fv", decl="void uShape__Fv()"),
	Ident(addr=0x80152C30, name="GetArea__Fv", decl="long GetArea__Fv()"),
	Ident(addr=0x80152C8C, name="L4drawRoom__Fiiii", decl="void L4drawRoom__Fiiii(int x, int y, int width, int height)"),
	Ident(addr=0x80152CF4, name="L4checkRoom__Fiiii", decl="unsigned char L4checkRoom__Fiiii(int x, int y, int width, int height)"),
	Ident(addr=0x80152D90, name="L4roomGen__Fiiiii", decl="void L4roomGen__Fiiiii(int x, int y, int w, int h, int dir)"),
	Ident(addr=0x80153078, name="L4firstRoom__Fv", decl="void L4firstRoom__Fv()"),
	Ident(addr=0x80153284, name="L4SaveQuads__Fv", decl="void L4SaveQuads__Fv()"),
	Ident(addr=0x80153344, name="DRLG_L4SetRoom__FPUcii", decl="void DRLG_L4SetRoom__FPUcii(unsigned char *pSetPiece, int rx1, int ry1)"),
	Ident(addr=0x80153418, name="DRLG_LoadDiabQuads__FUc", decl="void DRLG_LoadDiabQuads__FUc(unsigned char preflag)"),
	Ident(addr=0x80153614, name="DRLG_L4PlaceMiniSet__FPCUciiiiii", decl="unsigned char DRLG_L4PlaceMiniSet__FPCUciiiiii(unsigned char *miniset, int tmin, int tmax, int cx, int cy, int setview, int ldir)"),
	Ident(addr=0x80153A30, name="DRLG_L4FTVR__Fiiiii", decl="void DRLG_L4FTVR__Fiiiii(int i, int j, int x, int y, int d)"),
	Ident(addr=0x80153ED8, name="DRLG_L4FloodTVal__Fv", decl="void DRLG_L4FloodTVal__Fv()"),
	Ident(addr=0x801540F0, name="IsDURWall__Fc", decl="unsigned char IsDURWall__Fc(char d)"),
	Ident(addr=0x80154120, name="IsDLLWall__Fc", decl="unsigned char IsDLLWall__Fc(char dd)"),
	Ident(addr=0x80154150, name="DRLG_L4TransFix__Fv", decl="void DRLG_L4TransFix__Fv()"),
	Ident(addr=0x801544BC, name="DRLG_L4Corners__Fv", decl="void DRLG_L4Corners__Fv()"),
	Ident(addr=0x80154550, name="L4FixRim__Fv", decl="void L4FixRim__Fv()"),
	Ident(addr=0x8015458C, name="DRLG_L4GeneralFix__Fv", decl="void DRLG_L4GeneralFix__Fv()"),
	Ident(addr=0x80154630, name="DRLG_L4SetWalls__Fv", decl="void DRLG_L4SetWalls__Fv()"),
	Ident(addr=0x801546E0, name="DRLG_L4__Fi", decl="void DRLG_L4__Fi(int entry)"),
	Ident(addr=0x80154FE0, name="DRLG_L4Pass3__Fv", decl="void DRLG_L4Pass3__Fv()"),
	Ident(addr=0x801551F8, name="CreateL4Dungeon__FUii", decl="void CreateL4Dungeon__FUii(unsigned int rseed, int entry)"),

	# diabpsx/source/setmaps.cpp
	Ident(addr=0x801552D8, name="ObjIndex__Fii", decl="int ObjIndex__Fii(int x, int y)"),
	Ident(addr=0x8015538C, name="AddSKingObjs__Fv", decl="void AddSKingObjs__Fv()"),
	Ident(addr=0x801554BC, name="AddSChamObjs__Fv", decl="void AddSChamObjs__Fv()"),
	Ident(addr=0x80155538, name="AddVileObjs__Fv", decl="void AddVileObjs__Fv()"),
	Ident(addr=0x801555E4, name="DRLG_SetMapTrans__FPc", decl="void DRLG_SetMapTrans__FPc(char *sFileName)"),
	Ident(addr=0x801556A8, name="LoadSetMap__Fv", decl="void LoadSetMap__Fv()"),

	# diabpsx/source/choosem.cpp
	Ident(addr=0x80155A04, name="CM_QuestToBitPattern__Fi", decl="unsigned long CM_QuestToBitPattern__Fi(int QuestNum)"),
	Ident(addr=0x80155ADC, name="CM_ShowMonsterList__Fii", decl="void CM_ShowMonsterList__Fii(int Level, int List)"),
	Ident(addr=0x80155AE4, name="CM_ChooseMonsterList__FiUl", decl="int CM_ChooseMonsterList__FiUl(int Level, unsigned long QuestsNeededMask)"),
	Ident(addr=0x80155B84, name="NoUiListChoose__FiUl", decl="int NoUiListChoose__FiUl(int Level, unsigned long QuestsNeededMask)"),
	Ident(addr=0x80155B8C, name="ChooseTask__FP4TASK", decl="void ChooseTask__FP4TASK(struct TASK *T)"),
	Ident(addr=0x80155C5C, name="ShowTask__FP4TASK", decl="void ShowTask__FP4TASK(struct TASK *T)"),
	Ident(addr=0x80155E8C, name="GetListsAvailable__FiUlPUc", decl="int GetListsAvailable__FiUlPUc(int Level, unsigned long QuestsNeededMask, unsigned char *ListofLists)"),

	# diabpsx/source/preobj.cpp
	Ident(addr=0x80155FD8, name="AddL1Door__Fiiii", decl="void AddL1Door__Fiiii(int i, int x, int y, int ot)"),
	Ident(addr=0x801560C0, name="AddSCambBook__Fi", decl="void AddSCambBook__Fi(int i)"),
	Ident(addr=0x80156160, name="AddChest__Fii", decl="void AddChest__Fii(int i, int t)"),
	Ident(addr=0x80156330, name="AddL2Door__Fiiii", decl="void AddL2Door__Fiiii(int i, int x, int y, int ot)"),
	Ident(addr=0x8015647C, name="AddL3Door__Fiiii", decl="void AddL3Door__Fiiii(int i, int x, int y, int ot)"),
	Ident(addr=0x80156510, name="AddSarc__Fi", decl="void AddSarc__Fi(int i)"),
	Ident(addr=0x801565D8, name="AddFlameTrap__Fi", decl="void AddFlameTrap__Fi(int i)"),
	Ident(addr=0x80156634, name="AddTrap__Fii", decl="void AddTrap__Fii(int i, int ot)"),
	Ident(addr=0x80156728, name="AddArmorStand__Fi", decl="void AddArmorStand__Fi(int i)"),
	Ident(addr=0x801567B0, name="AddObjLight__Fii", decl="void AddObjLight__Fii(int i, int r)"),
	Ident(addr=0x80156878, name="AddBarrel__Fii", decl="void AddBarrel__Fii(int i, int ot)"),
	Ident(addr=0x80156920, name="AddShrine__Fi", decl="void AddShrine__Fi(int i)"),
	Ident(addr=0x80156A68, name="AddBookcase__Fi", decl="void AddBookcase__Fi(int i)"),
	Ident(addr=0x80156AC0, name="AddBookstand__Fi", decl="void AddBookstand__Fi(int i)"),
	Ident(addr=0x80156B08, name="AddBloodFtn__Fi", decl="void AddBloodFtn__Fi(int i)"),
	Ident(addr=0x80156B50, name="AddPurifyingFountain__Fi", decl="void AddPurifyingFountain__Fi(int i)"),
	Ident(addr=0x80156C0C, name="AddGoatShrine__Fi", decl="void AddGoatShrine__Fi(int i)"),
	Ident(addr=0x80156C54, name="AddCauldron__Fi", decl="void AddCauldron__Fi(int i)"),
	Ident(addr=0x80156C9C, name="AddMurkyFountain__Fi", decl="void AddMurkyFountain__Fi(int i)"),
	Ident(addr=0x80156D58, name="AddTearFountain__Fi", decl="void AddTearFountain__Fi(int i)"),
	Ident(addr=0x80156DA0, name="AddDecap__Fi", decl="void AddDecap__Fi(int i)"),
	Ident(addr=0x80156E14, name="AddVilebook__Fi", decl="void AddVilebook__Fi(int i)"),
	Ident(addr=0x80156E64, name="AddMagicCircle__Fi", decl="void AddMagicCircle__Fi(int i)"),
	Ident(addr=0x80156ED8, name="AddBrnCross__Fi", decl="void AddBrnCross__Fi(int i)"),
	Ident(addr=0x80156F20, name="AddPedistal__Fi", decl="void AddPedistal__Fi(int i)"),
	Ident(addr=0x80156FC8, name="AddStoryBook__Fi", decl="void AddStoryBook__Fi(int i)"),
	Ident(addr=0x80157148, name="AddWeaponRack__Fi", decl="void AddWeaponRack__Fi(int i)"),
	Ident(addr=0x801571D0, name="AddTorturedBody__Fi", decl="void AddTorturedBody__Fi(int i)"),
	Ident(addr=0x80157248, name="AddFlameLvr__Fi", decl="void AddFlameLvr__Fi(int i)"),
	Ident(addr=0x80157288, name="GetRndObjLoc__FiRiT1", decl="void GetRndObjLoc__FiRiT1(int randarea, int *xx, int *yy)"),
	Ident(addr=0x8015738C, name="AddMushPatch__Fv", decl="void AddMushPatch__Fv()"),
	Ident(addr=0x80157480, name="AddSlainHero__Fv", decl="void AddSlainHero__Fv()"),
	Ident(addr=0x801574C0, name="RndLocOk__Fii", decl="unsigned char RndLocOk__Fii(int xp, int yp)"),
	Ident(addr=0x801575D8, name="TrapLocOk__Fii", decl="unsigned char TrapLocOk__Fii(int xp, int yp)"),
	Ident(addr=0x8015762C, name="InitRndLocObj__Fiii", decl="void InitRndLocObj__Fiii(int min, int max, int objtype)"),
	Ident(addr=0x801577AC, name="InitRndLocBigObj__Fiii", decl="void InitRndLocBigObj__Fiii(int min, int max, int objtype)"),
	Ident(addr=0x8015796C, name="InitRndLocObj5x5__Fiii", decl="void InitRndLocObj5x5__Fiii(int min, int max, int objtype)"),
	Ident(addr=0x80157A88, name="SetMapObjects__FPUcii", decl="void SetMapObjects__FPUcii(unsigned char *pMap, int startx, int starty)"),
	Ident(addr=0x80157D28, name="ClrAllObjects__Fv", decl="void ClrAllObjects__Fv()"),
	Ident(addr=0x80157E18, name="AddTortures__Fv", decl="void AddTortures__Fv()"),
	Ident(addr=0x80157F98, name="AddCandles__Fv", decl="void AddCandles__Fv()"),
	Ident(addr=0x80158020, name="AddBookLever__Fiiiiiiiii", decl="void AddBookLever__Fiiiiiiiii(int lx1, int ly1, int lx2, int ly2, int x1, int y1, int x2, int y2, int msg)"),
	Ident(addr=0x80158214, name="InitRndBarrels__Fv", decl="void InitRndBarrels__Fv()"),
	Ident(addr=0x801583A0, name="AddL1Objs__Fiiii", decl="void AddL1Objs__Fiiii(int x1, int y1, int x2, int y2)"),
	Ident(addr=0x801584AC, name="AddL2Objs__Fiiii", decl="void AddL2Objs__Fiiii(int x1, int y1, int x2, int y2)"),
	Ident(addr=0x801585A8, name="AddL3Objs__Fiiii", decl="void AddL3Objs__Fiiii(int x1, int y1, int x2, int y2)"),
	Ident(addr=0x80158688, name="WallTrapLocOk__Fii", decl="unsigned char WallTrapLocOk__Fii(int xp, int yp)"),
	Ident(addr=0x801586E0, name="TorchLocOK__Fii", decl="unsigned char TorchLocOK__Fii(int xp, int yp)"),
	Ident(addr=0x80158710, name="AddL2Torches__Fv", decl="void AddL2Torches__Fv()"),
	Ident(addr=0x801588AC, name="AddObjTraps__Fv", decl="void AddObjTraps__Fv()"),
	Ident(addr=0x80158B34, name="AddChestTraps__Fv", decl="void AddChestTraps__Fv()"),
	Ident(addr=0x80158C70, name="LoadMapObjects__FPUciiiiiii", decl="void LoadMapObjects__FPUciiiiiii(unsigned char *pMap, int startx, int starty, int x1, int y1, int w, int h, int leveridx)"),
	Ident(addr=0x80158DDC, name="AddDiabObjs__Fv", decl="void AddDiabObjs__Fv()"),
	Ident(addr=0x80158F30, name="AddStoryBooks__Fv", decl="void AddStoryBooks__Fv()"),
	Ident(addr=0x80159078, name="AddHookedBodies__Fi", decl="void AddHookedBodies__Fi(int freq)"),
	Ident(addr=0x8015926C, name="AddL4Goodies__Fv", decl="void AddL4Goodies__Fv()"),
	Ident(addr=0x8015931C, name="AddLazStand__Fv", decl="void AddLazStand__Fv()"),
	Ident(addr=0x801594A8, name="saveplrpos__Fv", decl="void saveplrpos__Fv()"),
	Ident(addr=0x80159564, name="restoreplrpos__Fv", decl="void restoreplrpos__Fv()"),
	Ident(addr=0x801595D4, name="InitObjects__Fv", decl="void InitObjects__Fv()"),
	Ident(addr=0x80159C74, name="PreObjObjAddSwitch__Fiiii", decl="void PreObjObjAddSwitch__Fiiii(int ot, int ox, int oy, int oi)"),

	# diabpsx/source/gendung.cpp
	Ident(addr=0x80159EDC, name="FillSolidBlockTbls__Fv", decl="void FillSolidBlockTbls__Fv()"),
	Ident(addr=0x8015A068, name="SetDungeonMicros__Fv", decl="void SetDungeonMicros__Fv()"),
	Ident(addr=0x8015A070, name="DRLG_InitTrans__Fv", decl="void DRLG_InitTrans__Fv()"),
	Ident(addr=0x8015A0E4, name="DRLG_RectTrans__Fiiii", decl="void DRLG_RectTrans__Fiiii(int x1, int y1, int x2, int y2)"),
	Ident(addr=0x8015A158, name="DRLG_CopyTrans__Fiiii", decl="void DRLG_CopyTrans__Fiiii(int sx, int sy, int dx, int dy)"),
	Ident(addr=0x8015A1A0, name="DRLG_ListTrans__FiPUc", decl="void DRLG_ListTrans__FiPUc(int num, unsigned char *List)"),
	Ident(addr=0x8015A214, name="DRLG_AreaTrans__FiPUc", decl="void DRLG_AreaTrans__FiPUc(int num, unsigned char *List)"),
	Ident(addr=0x8015A2A4, name="DRLG_InitSetPC__Fv", decl="void DRLG_InitSetPC__Fv()"),
	Ident(addr=0x8015A2BC, name="DRLG_SetPC__Fv", decl="void DRLG_SetPC__Fv()"),
	Ident(addr=0x8015A35C, name="Make_SetPC__Fiiii", decl="void Make_SetPC__Fiiii(int x, int y, int w, int h)"),
	Ident(addr=0x8015A3EC, name="DRLG_WillThemeRoomFit__FiiiiiPiT5", decl="unsigned char DRLG_WillThemeRoomFit__FiiiiiPiT5(int floor, int x, int y, int minSize, int maxSize, int *width, int *height)"),
	Ident(addr=0x8015A6B4, name="DRLG_CreateThemeRoom__Fi", decl="void DRLG_CreateThemeRoom__Fi(int themeIndex)"),
	Ident(addr=0x8015B6B8, name="DRLG_PlaceThemeRooms__FiiiiUc", decl="void DRLG_PlaceThemeRooms__FiiiiUc(int minSize, int maxSize, int floor, int freq, int rndSize)"),
	Ident(addr=0x8015B958, name="DRLG_HoldThemeRooms__Fv", decl="void DRLG_HoldThemeRooms__Fv()"),
	Ident(addr=0x8015BAFC, name="SkipThemeRoom__Fii", decl="unsigned char SkipThemeRoom__Fii(int x, int y)"),
	Ident(addr=0x8015BBC8, name="InitLevels__Fv", decl="void InitLevels__Fv()"),

	# diabpsx/source/themes.cpp
	Ident(addr=0x8015BC0C, name="TFit_Shrine__Fi", decl="unsigned char TFit_Shrine__Fi(int i)"),
	Ident(addr=0x8015BEFC, name="TFit_Obj5__Fi", decl="unsigned char TFit_Obj5__Fi(int t)"),
	Ident(addr=0x8015C0C0, name="TFit_SkelRoom__Fi", decl="unsigned char TFit_SkelRoom__Fi(int t)"),
	Ident(addr=0x8015C170, name="TFit_GoatShrine__Fi", decl="unsigned char TFit_GoatShrine__Fi(int t)"),
	Ident(addr=0x8015C208, name="CheckThemeObj3__Fiiii", decl="unsigned char CheckThemeObj3__Fiiii(int xp, int yp, int t, int f)"),
	Ident(addr=0x8015C354, name="TFit_Obj3__Fi", decl="unsigned char TFit_Obj3__Fi(int t)"),
	Ident(addr=0x8015C414, name="CheckThemeReqs__Fi", decl="unsigned char CheckThemeReqs__Fi(int t)"),
	Ident(addr=0x8015C4E0, name="SpecialThemeFit__Fii", decl="unsigned char SpecialThemeFit__Fii(int i, int t)"),
	Ident(addr=0x8015C6BC, name="CheckThemeRoom__Fi", decl="unsigned char CheckThemeRoom__Fi(int tv)"),
	Ident(addr=0x8015C980, name="InitThemes__Fv", decl="void InitThemes__Fv()"),
	Ident(addr=0x8015CCCC, name="HoldThemeRooms__Fv", decl="void HoldThemeRooms__Fv()"),
	Ident(addr=0x8015CDB0, name="PlaceThemeMonsts__Fii", decl="void PlaceThemeMonsts__Fii(int t, int f)"),
	Ident(addr=0x8015CF34, name="Theme_Barrel__Fi", decl="void Theme_Barrel__Fi(int t)"),
	Ident(addr=0x8015D090, name="Theme_Shrine__Fi", decl="void Theme_Shrine__Fi(int t)"),
	Ident(addr=0x8015D178, name="Theme_MonstPit__Fi", decl="void Theme_MonstPit__Fi(int t)"),
	Ident(addr=0x8015D2BC, name="Theme_SkelRoom__Fi", decl="void Theme_SkelRoom__Fi(int t)"),
	Ident(addr=0x8015D5F8, name="Theme_Treasure__Fi", decl="void Theme_Treasure__Fi(int t)"),
	Ident(addr=0x8015D83C, name="Theme_Library__Fi", decl="void Theme_Library__Fi(int t)"),
	Ident(addr=0x8015DAC0, name="Theme_Torture__Fi", decl="void Theme_Torture__Fi(int t)"),
	Ident(addr=0x8015DC18, name="Theme_BloodFountain__Fi", decl="void Theme_BloodFountain__Fi(int t)"),
	Ident(addr=0x8015DC8C, name="Theme_Decap__Fi", decl="void Theme_Decap__Fi(int t)"),
	Ident(addr=0x8015DDE4, name="Theme_PurifyingFountain__Fi", decl="void Theme_PurifyingFountain__Fi(int t)"),
	Ident(addr=0x8015DE58, name="Theme_ArmorStand__Fi", decl="void Theme_ArmorStand__Fi(int t)"),
	Ident(addr=0x8015DFD4, name="Theme_GoatShrine__Fi", decl="void Theme_GoatShrine__Fi(int t)"),
	Ident(addr=0x8015E108, name="Theme_Cauldron__Fi", decl="void Theme_Cauldron__Fi(int t)"),
	Ident(addr=0x8015E17C, name="Theme_MurkyFountain__Fi", decl="void Theme_MurkyFountain__Fi(int t)"),
	Ident(addr=0x8015E1F0, name="Theme_TearFountain__Fi", decl="void Theme_TearFountain__Fi(int t)"),
	Ident(addr=0x8015E264, name="Theme_BrnCross__Fi", decl="void Theme_BrnCross__Fi(int t)"),
	Ident(addr=0x8015E3C0, name="Theme_WeaponRack__Fi", decl="void Theme_WeaponRack__Fi(int t)"),
	Ident(addr=0x8015E53C, name="UpdateL4Trans__Fv", decl="void UpdateL4Trans__Fv()"),
	Ident(addr=0x8015E598, name="CreateThemeRooms__Fv", decl="void CreateThemeRooms__Fv()"),

	# diabpsx/source/preport.cpp
	Ident(addr=0x8015E77C, name="InitPortals__Fv", decl="void InitPortals__Fv()"),

	# diabpsx/source/prequest.cpp
	Ident(addr=0x8015E7DC, name="InitQuests__Fv", decl="void InitQuests__Fv()"),
	Ident(addr=0x8015ED8C, name="DrawButcher__Fv", decl="void DrawButcher__Fv()"),
	Ident(addr=0x8015EDD0, name="DrawSkelKing__Fiii", decl="void DrawSkelKing__Fiii(int q, int x, int y)"),
	Ident(addr=0x8015EE64, name="DrawWarLord__Fii", decl="void DrawWarLord__Fii(int x, int y)"),
	Ident(addr=0x8015EF60, name="DrawSChamber__Fiii", decl="void DrawSChamber__Fiii(int q, int x, int y)"),
	Ident(addr=0x8015F09C, name="DrawLTBanner__Fii", decl="void DrawLTBanner__Fii(int x, int y)"),
	Ident(addr=0x8015F178, name="DrawBlind__Fii", decl="void DrawBlind__Fii(int x, int y)"),
	Ident(addr=0x8015F254, name="DrawBlood__Fii", decl="void DrawBlood__Fii(int x, int y)"),
	Ident(addr=0x8015F334, name="DRLG_CheckQuests__Fii", decl="void DRLG_CheckQuests__Fii(int x, int y)"),

	# diabpsx/source/preinv.cpp
	Ident(addr=0x8015F470, name="InitInv__Fv", decl="void InitInv__Fv()"),

	# diabpsx/source/preauto.cpp
	Ident(addr=0x8015F4C4, name="InitAutomap__Fv", decl="void InitAutomap__Fv()"),
	Ident(addr=0x8015F6BC, name="InitAutomapOnce__Fv", decl="void InitAutomapOnce__Fv()"),

	# diabpsx/source/premon.cpp
	Ident(addr=0x8015F6E8, name="SwapMonsterType__FPi", decl="void SwapMonsterType__FPi(int *oldmt)"),
	Ident(addr=0x8015F75C, name="MonstPlace__Fii", decl="unsigned char MonstPlace__Fii(int xp, int yp)"),
	Ident(addr=0x8015F828, name="InitMonsterGFX__Fi", decl="void InitMonsterGFX__Fi(int monst)"),
	Ident(addr=0x8015F900, name="PlaceMonster__Fiiii", decl="void PlaceMonster__Fiiii(int i, int mtype, int x, int y)"),
	Ident(addr=0x8015F98C, name="AddMonsterType__Fii", decl="int AddMonsterType__Fii(int type, int placeflag)"),
	Ident(addr=0x8015FA88, name="GetMonsterTypes__FUl", decl="void GetMonsterTypes__FUl(unsigned long QuestMask)"),
	Ident(addr=0x8015FB48, name="ClrAllMonsters__Fv", decl="void ClrAllMonsters__Fv()"),
	Ident(addr=0x8015FC80, name="InitLevelMonsters__Fv", decl="void InitLevelMonsters__Fv()"),
	Ident(addr=0x8015FD04, name="GetLevelMTypes__Fv", decl="void GetLevelMTypes__Fv()"),
	Ident(addr=0x801601D8, name="PlaceQuestMonsters__Fv", decl="void PlaceQuestMonsters__Fv()"),
	Ident(addr=0x8016059C, name="LoadDiabMonsts__Fv", decl="void LoadDiabMonsts__Fv()"),
	Ident(addr=0x801606AC, name="PlaceGroup__FiiUci", decl="void PlaceGroup__FiiUci(int mtype, int num, unsigned char leaderf, int leader)"),
	Ident(addr=0x80160CA0, name="SetMapMonsters__FPUcii", decl="void SetMapMonsters__FPUcii(unsigned char *pMap, int startx, int starty)"),
	Ident(addr=0x80160ED4, name="InitMonsters__Fv", decl="void InitMonsters__Fv()"),
	Ident(addr=0x80161288, name="PlaceUniqueMonst__Fiii", decl="void PlaceUniqueMonst__Fiii(int uniqindex, int miniontype, int unpackfilesize)"),
	Ident(addr=0x80161BCC, name="PlaceUniques__Fv", decl="void PlaceUniques__Fv()"),
	Ident(addr=0x80161D5C, name="PreSpawnSkeleton__Fv", decl="int PreSpawnSkeleton__Fv()"),
	Ident(addr=0x80161E94, name="decode_enemy__Fii", decl="void decode_enemy__Fii(int m, int enemy)"),
	Ident(addr=0x80161FB0, name="IsGoat__Fi", decl="unsigned char IsGoat__Fi(int mt)"),

	# diabpsx/source/premiss.cpp
	Ident(addr=0x80161FDC, name="InitMissiles__Fv", decl="void InitMissiles__Fv()"),

	# diabpsx/source/pretrigs.cpp
	Ident(addr=0x801621AC, name="InitNoTriggers__Fv", decl="void InitNoTriggers__Fv()"),
	Ident(addr=0x801621D0, name="InitTownTriggers__Fv", decl="void InitTownTriggers__Fv()"),
	Ident(addr=0x80162530, name="InitL1Triggers__Fv", decl="void InitL1Triggers__Fv()"),
	Ident(addr=0x8016265C, name="InitL2Triggers__Fv", decl="void InitL2Triggers__Fv()"),
	Ident(addr=0x80162824, name="InitL3Triggers__Fv", decl="void InitL3Triggers__Fv()"),
	Ident(addr=0x801629B0, name="InitL4Triggers__Fv", decl="void InitL4Triggers__Fv()"),
	Ident(addr=0x80162BF8, name="InitSKingTriggers__Fv", decl="void InitSKingTriggers__Fv()"),
	Ident(addr=0x80162C44, name="InitSChambTriggers__Fv", decl="void InitSChambTriggers__Fv()"),
	Ident(addr=0x80162C90, name="InitPWaterTriggers__Fv", decl="void InitPWaterTriggers__Fv()"),

	# diabpsx/source/prestore.cpp
	Ident(addr=0x80162CDC, name="InitStores__Fv", decl="void InitStores__Fv()"),
	Ident(addr=0x80162DD0, name="SetupTownStores__Fv", decl="void SetupTownStores__Fv()"),

	# diabpsx/source/premsg.cpp
	Ident(addr=0x80162FD4, name="DefragItems__FPUci", decl="void DefragItems__FPUci(unsigned char *ilist, int num)"),
	Ident(addr=0x8016301C, name="removellist__FPUcUc", decl="void removellist__FPUcUc(unsigned char *ilist, unsigned char val)"),
	Ident(addr=0x80163054, name="DeltaLoadLevel__Fv", decl="void DeltaLoadLevel__Fv()"),
]

for f in funcs:
	ida_name.set_name(f.addr, f.name)
