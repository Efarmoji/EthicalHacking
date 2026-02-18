from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'EthHack/home.html')



#_________________________________________________________________________________________________

def snippets_home(request):
    return render(request,'EthHack/Snippets/snippets_home.html')


def BlindSqlEnum(request):
    return render(request,'EthHack/Snippets/python/BlindSqlEnum.html')

def curl_json(request):
    return render(request,'EthHack/Snippets/linux/curl_json.html')


#_________________________________________________________________________________________________

def cve_home(request):
    return render(request,'EthHack/CVEs/cve.html')

def laravel_cve_2021_3129(request):
    return render(request,'EthHack/CVEs/cve/laravel-cve-2021-3129.html')

def Strapi_cve_2019_19609(request):
    return render(request,'EthHack/CVEs/cve/Strapi-cve-2019-19609.html')

def git_repo_CVE_2022_24439(request):
    return render(request,'EthHack/CVEs/cve/git_repo_cve_2022_24439.html')

def drupal_cve_2018_7600(request):
    return render(request,'EthHack/CVEs/cve/drupal_cve_2018_7600.html')

def dirty_socket(request):
    return render(request, 'EthHack/CVEs/cve/dirty_socket.html')

def image_magick(request):
    return render(request,'EthHack/CVEs/cve/imagemagick.html')

def js2py(request):
    return render(request,'EthHack/CVEs/cve/js2py.html')

def npbackup_cli(request):
    return render(request,'EthHack/CVEs/cve/npbackup-cli.html')


#_________________________________________________________________________________________________
def jargons(request):
    return render(request,'EthHack/Jargons/jargons-home.html')

def internet(request):
    return render(request,'EthHack/Jargons/pages/internet.html')

def ad(request):
    return render(request,'EthHack/Jargons/pages/ad.html')

#___________________________________________________________________________________________________

def phishing(request):
    return render(request,'EthHack/Phishing/phishing.html')

def vanish(request):
    return render(request,'EthHack/Phishing/vanish.html')

#_________________________________________________________________________________________________
def vulnerabilities(request):
    return render(request,'EthHack/Vulnerabilities/vulnerabilities-home.html')

def ssti(request):
    return render(request,'EthHack/Vulnerabilities/SSTI/SSTI.html')

def sqli(request):
    return render(request, 'EthHack/Vulnerabilities/SQLi/sqli_home.html')


def windows(request):
    return render(request,'EthHack/Vulnerabilities/windows/windows_home.html')


def path_hijack(request):
    return render(request,'EthHack/Vulnerabilities/code_vul/path_hijack.html')

def file_magick_numbers(request):
    return render(request,'EthHack/Vulnerabilities/web_vul/file_magick_numbers.html')


def xee(request):
    return render(request, 'EthHack/Vulnerabilities/web_vul/xee.html')

def esc4(request):
    return render(request,'EthHack/Vulnerabilities/ad/esc4.html')

def esc9(request):
    return render(request,'EthHack/Vulnerabilities/ad/esc9.html')

def ADCS(request):
    return render(request,'EthHack/Vulnerabilities/ad/ADCS.html')

def GPO(request):
    return render(request,'EthHack/Vulnerabilities/ad/GPO.html')
#_________________________________________________________________________________________________
def tools(request):
    return render(request,'EthHack/tools/tools-home.html')

def docker(request):
    return render(request,'EthHack/tools/environment/docker.html')

def lxd(request):
    return render(request,'EthHack/tools/environment/lxd.html')

def string_check(request):
    return render(request, 'EthHack/tools/pages/utils/string_check.html')

def searchsploit(request):
    return render(request,'EthHack/tools/pages/Enumeration/searchsploit.html')

def hashcat_view(request):
    return render(request,'EthHack/tools/pages/Cracker/hashcat.html')

def ssh(request):
    return render(request,'EthHack/tools/pages/remote_access/ssh.html')

def wpscan(request):
    return render(request,'EthHack/tools/pages/Enumeration/wpscan.html')

def nikto(request):
    return render(request,'EthHack/tools/pages/Enumeration/nikto.html')

def jd_gui(request):
    return render(request,'EthHack/tools/pages/Analyzer/jd_gui.html')

def hash_identifier(request):
    return render(request,'EthHack/tools/pages/Cracker/hash_identifier.html')

def git(request):
    return render(request,'EthHack/tools/pages/Enumeration/git.html')

def sqlmap(request):
    return render(request,'EthHack/tools/pages/Enumeration/sqlmap.html')


def ltrace(request):
    return render(request,'EthHack/tools/pages/Binary_analysis/ltrace.html')

def nmap(request):
    return render(request, 'EthHack/tools/pages/Enumeration/nmap.html')

def snmpwalk(request):
    return render(request,'EthHack/tools/pages/remote_access/snmpwalk.html')


def ffuf(request):
    return render(request,'EthHack/tools/pages/Enumeration/ffuf.html')


def socat(request):
    return render(request,'EthHack/tools/pages/remote_access/socat.html')


def chisel(request):
    return render(request,'EthHack/tools/pages/remote_access/chisel.html')

def curl(request):
    return render(request,'EthHack/tools/pages/request_handler/curl.html')


def xxd(request):
    return render(request,'EthHack/tools/pages/utils/xxd.html')

def openssl(request):
    return render(request,'EthHack/tools/pages/remote_access/openssl.html')

def grep(request):
    return render(request,'EthHack/tools/pages/utils/grep.html')

def chown(request):
    return render(request,'EthHack/tools/pages/utils/chown.html')

def ps(request):
    return render(request,'EthHack/tools/pages/Binary_analysis/ps.html')


def identify(request):
    return render(request,'EthHack/tools/pages/Binary_analysis/identify.html')


def steghide(request):
    return render(request,'EthHack/tools/pages/Binary_analysis/steghide.html')


def scp(request):
    return render(request,'EthHack/tools/pages/remote_access/scp.html')


def gobuster(request):
    return render(request,'EthHack/tools/pages/Enumeration/gobuster.html')


def php_webshell(request):
    return render(request,'EthHack/tools/pages/malicious_codes/php_webshell.html')



def msfvenom(request):
    return render(request,'EthHack/tools/pages/payload_generator/msfvenom.html')

def nc64_exe(request):
    return render(request,'EthHack/tools/pages/remote_access/nc64_exe.html')


def multi_handler(request):
    return render(request,'EthHack/tools/pages/payload_generator/multi_handler.html')

def sqli_codes(request):
    return render(request,'EthHack/tools/pages/malicious_codes/sqli_codes.html')


def snmp_brute(request):
    return render(request,'EthHack/tools/pages/remote_access/snmp_brute.html')


def postgres(request):
    return render(request,'EthHack/tools/pages/malicious_codes/postgres.html')


def john(request):
    return render(request,'EthHack/tools/pages/cracker/john.html')

def nc(request):
    return render(request,'EthHack/tools/pages/remote_access/nc.html')

def mysql(request):
    return render(request,'EthHack/tools/pages/malicious_codes/mysql.html')

def hydra(request):
    return render(request,'EthHack/tools/pages/cracker/hydra.html')

def cewl(request):
    return render(request,'EthHack/tools/pages/Enumeration/cewl.html')

def gcc(request):
    return render(request,'EthHack/tools/pages/payload_generator/gcc.html')

def ftp(request):
    return render(request,'EthHack/tools/pages/remote_access/ftp.html')
def mdb(request):
    return render(request,'EthHack/tools/pages/Analyzer/mdb.html')

def seven_zip(request):
    return render(request,'EthHack/tools/pages/Analyzer/7z.html')

def windows_cmd(request):
    return render(request,'EthHack/tools/windows_cmd.html')

def AD_priv(request):
    return render(request,'EthHack/tools/AD_priv.html')

def cms_revshell(request):
    return render(request,'EthHack/tools/cms_revshell.html')

def LFI(request):
    return render(request,'EthHack/tools/LFI.html')

def potato_family(request):
    return render(request,'EthHack/tools/pages/windows/potato_family.html')

def enum4linux(request):
    return render(request,'EthHack/tools/pages/Enumeration/enum4linux.html')

def kpcli(request):
    return render(request,'EthHack/tools/pages/Analyzer/kpcli.html')

def nfs(request):
    return render(request,'EthHack/tools/pages/Enumeration/nfs.html')

def gpp_decrypt(request):
    return render(request,'EthHack/tools/pages/Cracker/gpp_decrypt.html')

def iconv(request):
    return render(request,'EthHack/tools/pages/utils/iconv.html')

def username_anarchy(request):
    return render(request,'EthHack/tools/pages/Enumeration/username-anarchy.html')

def mssql(request):
    return render(request,'EthHack/tools/pages/malicious_codes/mssql.html')

def windows_exploit_suggester(request):
    return render(request,'EthHack/tools/pages/Enumeration/windows-exploit-suggester.html')

def pwsafe(request):
    return render(request,'EthHack/tools/pages/Cracker/pwsafe.html')

def keepassxc_cli(request):
    return render(request,'EthHack/tools/pages/Cracker/keepassxc-cli.html')

def javac(request):
    return render(request,'EthHack/tools/pages/payload_generator/javac.html')

def firefox_decrypt(request):
    return render(request,'EthHack/tools/pages/Cracker/firefox_decrypt.html')

def awk(request):
    return render(request,'EthHack/tools/pages/utils/awk.html')

def dirsearch(request):
    return render(request,'EthHack/tools/pages/Enumeration/dirsearch.html')
def md5sum(request):
    return render(request,'EthHack/tools/pages/utils/md5sum.html')

def xfreerdp3(request):
    return render(request,'EthHack/tools/pages/remote_access/xfreerdp3.html')

def clipboard(request):
    return render(request,'EthHack/tools/pages/utils/clipboard.html')

def base64(request):
    return render(request,'EthHack/tools/pages/utils/base64.html')

def smbget(request):
    return render(request,'EthHack/tools/pages/remote_access/smbget.html')

def smdb(request):
    return render(request,'Ethhack/tools/pages/remote_access/smdb.html')

def docx2txt(request):
    return render(request,'EthHack/tools/pages/utils/docx2txt.html')

def packet_loss(request):
    return render(request,'EthHack/tools/pages/utils/packet_loss.html')

def java_jdb(request):
    return render(request,'EthHack/tools/pages/malicious_codes/java_jdb.html')

def wireshark(request):
    return render(request,'EthHack/tools/pages/request_handler/wireshark.html')

def exiftool(request):
    return render(request,'EthHack/tools/pages/binary_analysis/exiftool.html')

def burpsuite(request):
    return render(request,'EthHack/tools/pages/utils/burpsuite.html')

#----------------------- Tools for windows ---------------------------
def nxc(request):
    return render(request,'EthHack/tools/pages/windows/nxc.html')

def certipy(request):
    return render(request,'EthHack/tools/pages/windows/certipy.html')

def impacket_changepasswd(request):
    return render(request,'EthHack/tools/pages/windows/impacket-changepasswd.html')


def evil_winrm(request):
    return render(request,'EthHack/tools/pages/windows/evil_winrm.html')

def smbclient(request):
    return render(request,'EthHack/tools/pages/windows/smbclient.html')

def crackmapexec(request):
    return render(request,'EthHack/tools/pages/windows/crackmapexec.html')

def impacket_smbserver(request):
    return render(request,'EthHack/tools/pages/windows/impacket_smbserver.html')

def command(request):
    return render(request,'EthHack/tools/pages/windows/command.html')

def powerup(request):
    return render(request,'EthHack/tools/pages/windows/powerup.html')

def impacket_psexec(request):
    return render(request,'EthHack/tools/pages/windows/impacket_psexec.html')

def PowerView(request):
    return render(request,'EthHack/tools/pages/windows/PowerView.html')

def sc_exe(request):
    return render(request,'EthHack/tools/pages/windows/sc_exe.html')

def impacket_lookupsid(request):
    return render(request,'EthHack/tools/pages/windows/impacket-lookupsid.html')

def impacket_secretsdump(request):
    return render(request,'EthHack/tools/pages/windows/impacket-secretsdump.html')

def smbmap(request):
    return render(request,'EthHack/tools/pages/windows/smbmap.html')

def impacket_getadusers(request):
    return render(request,'EthHack/tools/pages/windows/impacket-GetADUsers.html')

def impacket_getuserrspns(request):
    return render(request,'EthHack/tools/pages/windows/impacket-GetUserSPNs.html')

def ldapsearch(request):
    return render(request,'EthHack/tools/pages/windows/ldapsearch.html')

def procdump(request):
    return render(request,'EthHack/tools/pages/windows/procdump.html')

def impacket_mssqlclient(request):
    return render(request,'EthHack/tools/pages/windows/impacket-mssqlclient.html')

def responder(request):
    return render(request,'EthHack/tools/pages/windows/responder.html')

def certify_exe(request):
    return render(request,'EthHack/tools/pages/windows/certify_exe.html')

def rubeus(request):
    return render(request,'EthHack/tools/pages/windows/rubeus.html')

def certipy_ad(request):
    return render(request,'EthHack/tools/pages/windows/certipy_ad.html')

def impacket_getupusers(request):
    return render(request,'EthHack/tools/pages/windows/impacket-getnpusers.html')

def print_spoofer(request):
    return render(request,'EthHack/tools/pages/windows/printspoofer.html')

def targetedKerberoast(request):
    return render(request,'EthHack/tools/pages/windows/targetedKerberoast.html')

def bloodyAD(request):
    return render(request,'EthHack/tools/pages/windows/bloodyAD.html')

def impacket_dpapi(request):
    return render(request,'EthHack/tools/pages/windows/impacket-dpapi.html')

def mimikatz(request):
    return render(request,'EthHack/tools/pages/windows/mimikatz.html')

def shrapgpoabuse(request):
    return render(request,'EthHack/tools/pages/windows/sharpgpoabuse.html')

def remmina(request):
    return render(request,'EthHack/tools/pages/windows/remmina.html')

def pypykatz(request):
    return render(request,'EthHack/tools/pages/windows/pypykatz.html')

def impacket_ntlmrelayx(request):
    return render(request,'EthHack/tools/pages/windows/impacket_ntlmrelayx.html')

def ntlm_theft(request):
    return render(request,'EthHack/tools/pages/windows/ntlm_theft.html')

def RunasCS(request):
    return render(request,'EthHack/tools/pages/windows/RunasCS.html')

def impacket_ticketer(request):
    return render(request,'EthHack/tools/pages/windows/impacket_ticketer.html')
#_________________________________________________________________________________________________
def sharphound(request):
    return render(request,'EthHack/tools/pages/ad/sharphound.html')

def net(request):
    return render(request,'EthHack/tools/pages/ad/net.html')
    
def bloodhound_python(request):
    return render(request,'EthHack/tools/pages/ad/bloodhound-python.html')
def pivot(request):
    return render(request,'EthHack/tools/pages/ad/pivot.html')

def linux_with_kerberos(request):
    return render(request,'EthHack/tools/pages/ad/linux_with_kerberos.html')

def fishing_instruction(request):
    return render(request,'EthHack/tools/pages/ad/fishing_instruction.html')

def ligolo_ng(request):
    return render(request,'EthHack/tools/pages/ad/ligolo_ng.html')

def virtual_computer_accounts(request):
    return render(request,'EthHack/tools/pages/ad/virtual_computer_accounts.html')

def golden_ticket(request):
    return render(request,'EthHack/tools/pages/ad/golden_ticket.html')
#_________________________________________________________________________________________________
def machines(request):
    return render(request,"EthHack/Machines/machines-home.html")

def topology(request):
    return render(request,"EthHack/Machines/machines/topology.html")

def armageddon(request):
    return render(request,"EthHack/Machines/machines/armageddon.html")

def editorial(request):
    return render(request,'EthHack/Machines/machines/editorial.html')

def horizontal(request):
    return render(request,'EthHack/Machines/machines/horizontal.html')

def blocky(request):
    return render(request,'EthHack/Machines/machines/blocky.html')

def down(request):
    return render(request,'EthHack/Machines/machines/down.html')

def titanic(request):
    return render(request, 'EthHack/Machines/machines/titanic.html')

def perfection(request):
    return render(request,'EthHack/Machines/machines/perfection.html')

def data(request):
    return render(request,'EthHack/Machines/machines/data.html')

def codePartTwo(request):
    return render(request, 'EthHack/Machines/machines/CodePartTwo.html')

def updown(request):
    return render(request, 'EthHack/Machines/machines/updown.html')


def soccer(request):
    return render(request,'EthHack/Machines/machines/soccer.html')

def usage(request):
    return render(request,'EthHack/Machines/machines/usage.html')

def builder(request):
    return render(request, 'EthHack/Machines/machines/builder.html')

def networked(request):
    return render(request, 'EthHack/Machines/machines/networked.html')

def pandora(request):
    return render(request,'EthHack/Machines/machines/pandora.html')


def magick(request):
    return render(request,'EthHack/Machines/machines/magick.html')

def nibbles(request):
    return render(request,'EthHack/Machines/machines/nibbles.html')

def devoops(request):
    return render(request,'EthHack/Machines/machines/devoops.html')

def valentine(request):
    return render(request,'EthHack/Machines/machines/valentine.html')

def pilgrimage(request):
    return render(request,'EthHack/Machines/machines/pilgrimage.html')

def irked(request):
    return render(request,'EthHack/Machines/machines/irked.html')

def help(request):
    return render(request,'EthHack/Machines/machines/help.html')

def sea(request):
    return render(request,'EthHack/Machines/machines/sea.html')

def openadmin(request):
    return render(request,'EthHack/Machines/machines/openadmin.html')

def jarvis(request):
    return render(request,'EthHack/Machines/machines/jarvis.html')

def mentor(request):
    return render(request,'EthHack/Machines/machines/mentor.html')

def tabby(request):
    return render(request,'EthHack/Machines/machines/tabby.html')
#______________________________________    windows    _____________________________________________

def blue(request):
    return render(request,'EthHack/Machines/machines/windows/blue.html')

def retro(request):
    return render(request,'EthHack/Machines/machines/windows/retro.html')

def jerry(request):
    return render(request,'EthHack/Machines/machines/windows/jerry.html')

def buff(request):
    return render(request,'EthHack/Machines/machines/windows/buff.html')

def love(request):
    return render(request,'EthHack/Machines/machines/windows/love.html')

def netmon(request):
    return render(request,'EthHack/Machines/machines/windows/netmon.html')

def chatterbox(request):
    return render(request,'EthHack/Machines/machines/windows/chatterbox.html')

def mailing(request):
    return render(request,'EthHack/Machines/machines/windows/mailing.html')

def access(request):
    return render(request,'EthHack/Machines/machines/windows/access.html')

def bounty(request):
    return render(request,'EthHack/Machines/machines/windows/bounty.html')

def jeeves(request):
    return render(request,'EthHack/Machines/machines/windows/jeeves.html')

def remote(request):
    return render(request,'EthHack/Machines/machines/windows/remote.html')

def heist(request):
    return render(request,'EthHack/Machines/machines/windows/heist.html')

def secnotes(request):
    return render(request,'EthHack/Machines/machines/windows/secnotes.html')

def querier(request):
    return render(request,'EthHack/Machines/machines/windows/querier.html')

def arctic(request):
    return render(request,'EthHack/Machines/machines/windows/arctic.html')

def giddy(request):
    return render(request,'EthHack/Machines/machines/windows/giddy.html')

def sniper(request):
    return render(request,'EthHack/Machines/machines/windows/sniper.html')
#______________________________________    Active Directory   _____________________________________________
def AD_return(request):
    return render(request,'EthHack/Machines/machines/AD/return.html')

def cicada(request):
    return render(request,'EthHack/Machines/machines/AD/cicada.html')

def active(request):
    return render(request,'EthHack/Machines/machines/AD/active.html')

def timelapse(request):
    return render(request,'EthHack/Machines/machines/AD/timelapse.html')

def escape(request):
    return render(request,'EthHack/Machines/machines/AD/escape.html')

def sauna(request):
    return render(request,'EthHack/Machines/machines/AD/sauna.html')

def forest(request):
    return render(request,'EthHack/Machines/machines/AD/forest.html')

def monteverde(request):
    return render(request,'EthHack/Machines/machines/AD/monteverde.html')

def administrator(request):
    return render(request,'EthHack/Machines/machines/AD/administrator.html')

def escape2(request):
    return render(request,'EthHack/Machines/machines/AD/escape2.html')

def certified(request):
    return render(request,'EthHack/Machines/machines/AD/certified.html')

def puppy(request):
    return render(request,'EthHack/Machines/machines/AD/puppy.html')

def thefrizz(request):
    return render(request,'EthHack/Machines/machines/AD/thefrizz.html')

def blackfield(request):
    return render(request,'EthHack/Machines/machines/AD/blackfield.html')

def flight(request):
    return render(request,'EthHack/Machines/machines/AD/flight.html')
#______________________________________    PGPlay    _____________________________________________

def amaterasu(request):
    return render(request,'EthHack/Machines/machines/PG_Play/amaterasu.html')

def potato(request):
    return render(request,'EthHack/Machines/machines/PG_Play/potato.html')

def bsscute(request):
    return render(request,'EthHack/Machines/machines/PG_Play/bsscute.html')

def blogger(request):
    return render(request,'EthHack/Machines/machines/PG_Play/blogger.html')

def funboxeasyenum(request):
    return render(request,'EthHack/Machines/machines/PG_Play/funboxeasyenum.html')

def loly(request):
    return render(request,'EthHack/Machines/machines/PG_Play/loly.html')

def stapler(request):
    return render(request,'EthHack/Machines/machines/PG_Play/stapler.html')

def gaara(request):
    return render(request,'EthHack/Machines/machines/PG_Play/gaara.html')

def glasgowsmile(request):
    return render(request,'EthHack/Machines/machines/PG_Play/glasgowsmile.html')

def veteta1(request):
    return render(request,'EthHack/Machines/machines/PG_Play/vegeta1.html')

def monitoring(request):
    return render(request,'EthHack/Machines/machines/PG_Play/monitoring.html')

def katana(request):
    return render(request,'EthHack/Machines/machines/PG_Play/katana.html')

def driftingblue(request):
    return render(request,'EthHack/Machines/machines/PG_Play/driftingblue.html')


def seppuku(request):
    return render(request,'EthHack/Machines/machines/PG_Play/seppuku.html')

def election1(request):
    return render(request,'EthHack/Machines/machines/PG_Play/election1.html')

def sosimple(request):
    return render(request,'EthHack/Machines/machines/PG_Play/sosimple.html')

def BTRSys2_1(request):
    return render(request,'EthHack/Machines/machines/PG_Play/BTRSys2_1.html')

def tre(request):
    return render(request,'EthHack/Machines/machines/PG_Play/tre.html')

def dc_9(request):
    return render(request,'EthHack/Machines/machines/PG_Play/dc_9.html')

def insanityhosting(request):
    return render(request,'EthHack/Machines/machines/PG_Play/insanityhosting.html')
#______________________________________    OffSec labs    _____________________________________________

def ClamAV(request):
    return render(request,'EthHack/Machines/machines/PG_Practice/ClamAV.html')

def pelican(request):
    return render(request,'EthHack/Machines/machines/PG_Practice/pelican.html')

def payday(request):
    return render(request,'EthHack/Machines/machines/PG_Practice/payday.html')

def snookums(request):
    return render(request,'EthHack/Machines/machines/PG_Practice/snookums.html')

def bratarina(request):
    return render(request,'EthHack/Machines/machines/PG_Practice/bratarina.html')

def pg_nibbles(request):
    return render(request,'EthHack/Machines/machines/PG_Practice/nibbles.html')

def zenphoto(request):
    return render(request,'EthHack/Machines/machines/PG_Practice/zenphoto.html')

def hetemit(request):
    return render(request,'EthHack/Machines/machines/PG_Practice/hetemit.html')

#______________________________________    OffSec labs    _____________________________________________

def kevin(request):
    return render(request,'EthHack/Machines/machines/PG_Practice/windows/kevin.html')

def internal(request):
    return render(request,'EthHack/Machines/machines/PG_Practice/windows/internal.html')

def algenon(request):
    return render(request,'EthHack/Machines/machines/PG_Practice/windows/algernon.html')



#______________________________________    OffSec labs    _____________________________________________

def secura(request):
    return render(request,'EthHack/Machines/OffSec/secura.html')

def medtech(request):
    return render(request,'EthHack/Machines/OffSec/medtech.html')

def relia_home(request):
    return render(request,'EthHack/Machines/OffSec/relia_home.html')

def box249(request):
    return render(request,'EthHack/Machines/OffSec/relia/249.html')

def box248(request):
    return render(request,'EthHack/Machines/OffSec/relia/248.html')

def box247(request):
    return render(request,'EthHack/Machines/OffSec/relia/247.html')

def box246(request):
    return render(request,'EthHack/Machines/OffSec/relia/246.html')

def box245(request):
    return render(request,'EthHack/Machines/OffSec/relia/245.html')

def box191(request):
    return render(request,'EthHack/Machines/OffSec/relia/191.html')

def box6(request):
    return render(request,'EthHack/Machines/OffSec/relia/6.html')

def box7(request):
    return render(request,'EthHack/Machines/OffSec/relia/7.html')

def box14(request):
    return render(request,'EthHack/Machines/OffSec/relia/14.html')

def box15(request):
    return render(request,'EthHack/Machines/OffSec/relia/15.html')

def box19(request):
    return render(request,'EthHack/Machines/OffSec/relia/19.html')

def box20(request):
    return render(request,'EthHack/Machines/OffSec/relia/20.html')

def box21(request):
    return render(request,'EthHack/Machines/OffSec/relia/21.html')

def box30(request):
    return render(request,'EthHack/Machines/OffSec/relia/30.html')

def box189(request):
    return render(request,'EthHack/Machines/OffSec/relia/189.html')

def box250(request):
    return render(request,'EthHack/Machines/OffSec/relia/250.html')


def OSCP_B(request):
    return render(request,'EthHack/Machines/OffSec/oscp_b/oscp_b_home.html')

def box146(request):
    return render(request,'EthHack/Machines/OffSec/oscp_b/146.html')
def box147(request):
    return render(request,'EthHack/Machines/OffSec/oscp_b/147.html')
def box148(request):
    return render(request,'EthHack/Machines/OffSec/oscp_b/148.html')
def box149(request):
    return render(request,'EthHack/Machines/OffSec/oscp_b/149.html')
def box150(request):
    return render(request,'EthHack/Machines/OffSec/oscp_b/150.html')
def box151(request):
    return render(request,'EthHack/Machines/OffSec/oscp_b/151.html')


def oscp_a(request):
    return render(request,'EthHack/Machines/OffSec/oscp_a/table.html')

def box140(request):
    return render(request,'EthHack/Machines/OffSec/oscp_a/140.html')
def box141(request):
    return render(request,'EthHack/Machines/OffSec/oscp_a/141.html')
def box142(request):
    return render(request,'EthHack/Machines/OffSec/oscp_a/142.html')
def box143(request):
    return render(request,'EthHack/Machines/OffSec/oscp_a/143.html')
def box144(request):
    return render(request,'EthHack/Machines/OffSec/oscp_a/144.html')
def box145(request):
    return render(request,'EthHack/Machines/OffSec/oscp_a/145.html')


def laser(request):
    return render(request,'EthHack/Machines/OffSec/laser.html')

def poseidon(request):
    return render(request,'EthHack/Machines/OffSec/poseidon.html')
#______________________________________source-code-analyze_________________________________________
def laravel_source_code(request):
    return render(request,"EthHack/Code-Analyze/PHP/laravel_source_code.html")

def laravel_exploit_code(request):
    return render(request,'EthHack/Code-Analyze/Exploit/laravel_exploit_code.html')

def strapi_exploit_code(request):
    return render(request,'EthHack/Code-Analyze/Exploit/strapi_exploit_code.html')

def dirty_socket_code(request):
    return render(request,'EthHack/Code-Analyze/Exploit/dirty_socket_code.html')

def decrypt_py(request):
    return render(request,'EthHack/Code-Analyze/Python/decrypt_py.html')


#-------------------------------------MITM-----------------------------------------------#

def page_1(request):
    return render(request,'EthHack/MITM/1.html')


#------------------------------------LearnThrough-----------------------------------------#
def routing(request):
    return render(request,'EthHack/LearnThrough/routing.html')

def osiModel(request):
    return render(request,'EthHack/LearnThrough/routing/OSIModel.html')

def ip_routing(request):
    return render(request,'EthHack/LearnThrough/routing/2_IProuting.html')


#--------------------------------------Tips--------------------------------------------------
def tips(request):
    return render(request,'EthHack/tips/tips_home.html')\
    
def initial_access(request):
    return render(request,'EthHack/tips/history/initial_access.html')

def lateral_movement(request):
    return render(request,'EthHack/tips/history/lateral_movement.html')

def PrivEsc(request):
    return render(request,'EthHack/tips/history/privesc.html')

def file_extensions(request):
    return render(request,'EthHack/tips/others/file_extensions.html')