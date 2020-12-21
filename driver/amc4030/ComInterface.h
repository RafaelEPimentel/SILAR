#ifndef COM_INTERFACE_H_BY_TP_20170313
#define COM_INTERFACE_H_BY_TP_20170313

//#define CALLBACK_DEF			int
#define CALLBACK_DEF __declspec(dllexport) int WINAPI

//返回值	含义
//1	命令执行完毕，控制器已经正确接收，并返回了正确值给服务器端。
//-1	命令执行失败，命令被控制判断为非法，控制器拒绝执行此命令（有可能执行此命令的条件不具备）
//-2	命令参数检查没通过，命令执行失败
//-4	DLL与控制器通讯超时。
//-6	命令执行冲突，表示上一个命令还未完全执行，又有新命令来了。（表现为：一个接口调用还未返回，又开始调用新的接口了。多线程中比较普遍）。


CALLBACK_DEF	COM_API_SetComType(int nType);//设置通讯类型
CALLBACK_DEF	COM_API_OpenLink(int nID,int nBound);//打开连接。
CALLBACK_DEF	COM_API_GetMachineStatus(unsigned char* unStatus);//获取机器状态字。

CALLBACK_DEF	COM_API_ReadFileData(int nSrc,int StartAdd,int len,unsigned char* pOutput);
CALLBACK_DEF	COM_API_WriteFileData(int nSrc,int StartAdd,int len,unsigned char* pInput);

CALLBACK_DEF	COM_API_Jog(int nAxis,float fDis,float Speed);
CALLBACK_DEF	COM_API_Home(int nXAxisSet,int nYAxisSet,int nZAxisSet);
CALLBACK_DEF	COM_API_StartAutoRun(int nType,int nID);
CALLBACK_DEF	COM_API_StopAxis(int nXAxisSet,int nYAxisSet,int nZAxisSet);
CALLBACK_DEF	COM_API_StopAll();	
CALLBACK_DEF	COM_API_SetOutputBit(int OutputID,int nStatus);
CALLBACK_DEF	COM_API_GetLastError(unsigned int* dwErr);//
CALLBACK_DEF	COM_API_DowloadSystemCfg(char* iniPath);//
CALLBACK_DEF	COM_API_DowloadFile(char* szPath,int nType,int ShowProcess);
CALLBACK_DEF	COM_API_SendData(int nLen,unsigned char* pData);
CALLBACK_DEF	COM_API_ReadData(int nLen,unsigned char* pInput,unsigned char* pOutput);





#endif