package no.mechatronics.sfi.grpc_fmu

import no.mechatronics.sfi.grpc_fmu.misc.SocketAddress
import org.apache.commons.cli.DefaultParser
import org.apache.commons.cli.HelpFormatter
import org.apache.commons.cli.Options
import java.net.Socket
import javax.swing.JOptionPane

/**
 *
 * @author Lars Ivar Hatledal
 */
object InputParser {

    private const val HELP = "help"

    private const val REMOTE = "remote"
    private const val LOCAL_PORT = "localPort"

    @JvmStatic
    fun parse(args: Array<String>, action: (SocketAddress?, Int?) -> Unit)  {

        val options = Options().apply {

            addOption(HELP, false, "Prints this message")
            addOption(REMOTE, true, "Specify the IP address of the remote tracking server. E.g. ${"127.0.0.1:7000"}")
            addOption(LOCAL_PORT, true, "Manually specify the local port to use. E.g. 7777 (optional)")

        }

        val jarName = java.io.File(InputParser::class.java
                .protectionDomain.codeSource.location.path).name

        DefaultParser().parse(options, args).also { cmd ->
            if (cmd.hasOption(HELP)) {
                HelpFormatter().printHelp(jarName, options)
            } else {

                var localPort: Int? = null
                if (cmd.hasOption(LOCAL_PORT)) {
                    localPort = parseInt(cmd.getOptionValue(LOCAL_PORT))
                }

                val remote: SocketAddress? = cmd.getOptionValue(REMOTE).let {
                    if (it != null) {
                        parseAddress(it)
                    } else {
                        null
                    }
                }

                action.invoke(remote, localPort)

            }

        }

    }

    private fun parseAddress(value: String) : SocketAddress {

        val split = value.split(":")
        if (split.size != 2) {
            error("Wrong address format!")
        }

        val host = split[0]
        val port = parseInt(split[1])
        return SocketAddress(host, port)
    }

    private fun parseInt(value: String) : Int {
        try {
            return value.toInt()
        } catch (ex: NumberFormatException) {
            error("Wrong input format! Unable to parse port number from input: ${value}")
        }
    }

}

//object GUIParser {
//
//    fun parse() : SocketAddress? {
//
//        val input = JOptionPane.showInputDialog(null, "Input the IP address of the remote tracking server. E.g ${"127.0.0.1:7000"}")
//
//        val split = input.split(":")
//        if (split.size != 2) {
//            error("Wrong input format! Expected the following format: '${"hostAddress:port"}'")
//        }
//
//        val host = split[0]
//
//        try {
//
//            val port = split[1].toInt()
//            return SocketAddress(host, port)
//
//        } catch (ex: NumberFormatException) {
//            error("Wrong input format! Unable to parse port number from input: ${split[1]}")
//        }
//
//
//    }
//
//}

object ConsoleParser {

    private const val REMOTE_PORT = "port"
    private const val REMOTE_ADDRESS = "host"

    private const val LOCAL_PORT = "localPort"

    private const val HELP = "help"

    fun parse(args: Array<String>) : SocketAddress? {

        val options = Options().apply {

            addOption(HELP, false, "Prints this message")

            addOption(REMOTE_PORT, true, "Specify the port of the remote tracking server. E.g. 7000")
            addOption(REMOTE_ADDRESS, true, "Specify the host name of the remote tracking server. E.g. ${"127.0.0.1"}")

            addOption(LOCAL_PORT, true, "Specify the local port to use. E.g. 7777")

        }

        val cmd = DefaultParser().parse(options, args)

        if (cmd.hasOption(HELP)) {
            HelpFormatter().printHelp("", options)
            return null
        }

        if (!cmd.hasOption(REMOTE_PORT)) {
            error("No port given!")
        }

        if (!cmd.hasOption(REMOTE_ADDRESS)) {
            error("No host given!")
        }

        val address = cmd.getOptionValue(REMOTE_ADDRESS)!!
        val port: Int? = cmd.getOptionValue(REMOTE_PORT).let { portString ->
            try {
                portString.toInt()
            } catch (ex: NumberFormatException) {
                error("Wrong input format! Unable to parse port number from input: ${portString}")
            }
        }

        return SocketAddress(address, port!!)


    }

}