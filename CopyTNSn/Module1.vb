Imports System
Imports System.Configuration.ConfigurationManager
Imports System.Net

Module Module1
    Sub Main()

        Dim zURL As String = System.Configuration.ConfigurationManager.AppSettings.Get("zURL")
        Dim kamUlozit As String = System.Configuration.ConfigurationManager.AppSettings.Get("kamUlozit")
        Console.WriteLine("stahuji soubor z adresy:")
        Console.WriteLine(zURL)
        Console.WriteLine("a ulozim ho do:")
        Console.WriteLine(kamUlozit)
        Dim Webclient As New System.Net.WebClient
        Webclient.DownloadFile(zURL, kamUlozit)
    End Sub
End Module


